"""
Custom modules for the admin dashboard.

This package adds the following classes:

* :class:`AppIconList`
* :class:`CmsAppIconList`
* :class:`PersonalModule`
"""
from django.conf import settings
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.translation import ugettext as _
from admin_tools.utils import get_admin_site_name
from admin_tools.dashboard import modules
from fluent_dashboard import appsettings
from fluent_dashboard.appgroups import is_cms_app, sort_cms_models


class PersonalModule(modules.LinkList):
    """
    A simple module to display a welcome message.

    It renders the template ``fluent_dashboard/modules/personal.html``,
    unless the ``template`` variable is overwritten.
    The module overrides :class:`~admin_tools.dashboard.modules.LinkList`,
    allowing links to be added to the element.
    """
    # Set admin_tools defaults
    draggable = False
    deletable = False
    collapsible = False

    #: Define the title to display
    title = _('Welcome,')

    #: Define the template to render
    template = 'fluent_dashboard/modules/personal.html'

    def init_with_context(self, context):
        """
        Initializes the link list.
        """
        super(PersonalModule, self).init_with_context(context)

        current_user = context['request'].user
        site_name = get_admin_site_name(context)

        # Personalize
        self.title = _('Welcome,') + ' ' + (current_user.first_name or current_user.username)

        # Expose links
        self.password_link = reverse('%s:password_change' % site_name)
        self.logout_link = reverse('%s:logout' % site_name)

        try:
            self.pages_link = reverse('%s:ecms_cmsobject_changelist' % site_name)
        except NoReverseMatch:
            self.pages_link = None

    def is_empty(self):
        # Make sure the element is rendered.
        return False




class AppIconList(modules.AppList):
    """
    The list of applications, icon style.

    It uses the ``FLUENT_DASHBOARD_APP_ICONS`` setting to find application icons.
    """

    #: Specify the template to render
    template = 'fluent_dashboard/modules/app_icon_list.html'

    # Allow old Django 1.2 MEDIA_URL, but prefer STATIC_URL if it's set.
    #: The current static root (considered read only)
    icon_static_root = getattr(settings, 'STATIC_URL', settings.MEDIA_URL)
    #: The current theme folder (considerd read only)
    icon_theme_root = "{0}fluent_dashboard/{1}/".format(icon_static_root, appsettings.FLUENT_DASHBOARD_ICON_THEME)


    def init_with_context(self, context):
        """
        Initializes the icon list.
        """
        super(AppIconList, self).init_with_context(context)
        apps = self.children
        path_levels = context['request'].META['SCRIPT_NAME'].rstrip('/').count('/')

        # Standard model only has a title, change_url and add_url.
        # Restore the app_name and name, so icons can be matched.
        for app in apps:
            app_name = app['url'].strip('/').split('/')[-1]   # /admin/appname/
            app['name'] = app_name

            for model in app['models']:
                try:
                    model_name = model['change_url'].strip('/').split('/')[2 + path_levels]   # admin/appname/modelname
                    model['name'] = model_name
                    model['icon'] = self.get_icon_for_model(app_name, model_name) or appsettings.FLUENT_DASHBOARD_DEFAULT_ICON
                except ValueError:
                    model['icon'] = appsettings.FLUENT_DASHBOARD_DEFAULT_ICON

                # Automatically add STATIC_URL before relative icon paths.
                model['icon'] = self.get_icon_url(model['icon'])
                model['app_name'] = app_name


    def get_icon_for_model(self, app_name, model_name, default=None):
        """
        Return the icon for the given model.
        It reads the :ref:`FLUENT_DASHBOARD_APP_ICONS` setting.
        """
        key = "%s/%s" % (app_name, model_name)
        return appsettings.FLUENT_DASHBOARD_APP_ICONS.get(key, default)


    def get_icon_url(self, icon):
        """
        Replaces the "icon name" with a full usable URL.

        * When the icon is an absolute URL, it is used as-is.
        * When the icon contains a slash, it is relative from the ``STATIC_URL``.
        * Otherwise, it's relative to the theme url folder.
        """
        if not icon.startswith('/') \
        and not icon.startswith('http://') \
        and not icon.startswith('https://'):
            if '/' in icon:
                return self.icon_static_root + icon
            else:
                return self.icon_theme_root + icon
        else:
            return icon



class CmsAppIconList(AppIconList):
    """
    A variation of the :class:`AppIconList` class
    with a strong bias towards sorting CMS apps on top.
    """
    def init_with_context(self, context):
        """
        Initializes the icon list.
        """
        super(CmsAppIconList, self).init_with_context(context)
        apps = self.children

        cms_apps     = [a for a in apps if is_cms_app(a['name'])]
        non_cms_apps = [a for a in apps if a not in cms_apps]

        if cms_apps:
            # Group the models of all CMS apps in one group.
            cms_models = []
            for app in cms_apps:
                cms_models += app['models']

            sort_cms_models(cms_models)
            single_cms_app = {'name': "Modules", 'title': "Modules", 'url': "", 'models': cms_models}

            # Put remaining groups after the first CMS group.
            self.children = [single_cms_app] + non_cms_apps