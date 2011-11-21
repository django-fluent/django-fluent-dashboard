"""
Custom modules for the admin dashboard.

This package adds the following classes:

* :class:`AppIconList`
* :class:`CmsAppIconList`
* :class:`PersonalModule`
* :class:`CacheStatusGroup`
"""
import logging
import socket
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse, NoReverseMatch
from django.db.models.loading import get_model
from django.utils.translation import ugettext as _
from admin_tools.utils import get_admin_site_name
from admin_tools.dashboard import modules
from fluent_dashboard import appsettings
from fluent_dashboard.appgroups import is_cms_app, sort_cms_models


logger = logging.getLogger("fluent_dashboard.modules")


class PersonalModule(modules.LinkList):
    """
    A simple module to display a welcome message.

    .. image:: /images/personalmodule.png
       :width: 471px
       :height: 77px
       :alt: PersonalModule for django-fluent-dashboard

    It renders the template ``fluent_dashboard/modules/personal.html``,
    unless the ``template`` variable is overwritten.
    The module overrides :class:`~admin_tools.dashboard.modules.LinkList`,
    allowing links to be added to the element.
    The :ref:`FLUENT_DASHBOARD_CMS_PAGE_MODEL` setting is used to display a link to the pages module.
    If this setting is not defined, a general text will be displayed instead.
    """
    # Set admin_tools defaults
    draggable = False
    deletable = False
    collapsible = False

    #: Define the title to display
    title = _('Welcome,')

    #: The model to use for the CMS pages link.
    cms_page_model = appsettings.FLUENT_DASHBOARD_CMS_PAGE_MODEL

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
        self.pages_link = None
        self.pages_title = None
        self.password_link = reverse('%s:password_change' % site_name)
        self.logout_link = reverse('%s:logout' % site_name)

        if self.cms_page_model:
            try:
                app_label, model_name = self.cms_page_model
                model = get_model(app_label, model_name)
                self.pages_title = model._meta.verbose_name_plural.lower()
                self.pages_link = reverse('{site}:{app}_{model}_changelist'.format(site=site_name, app=app_label.lower(), model=model_name.lower()))
            except AttributeError:
                raise ImproperlyConfigured("The value {0} of FLUENT_DASHBOARD_CMS_PAGE_MODEL setting (or cms_page_model value) does not reffer to an existing model.".format(self.cms_page_model))
            except NoReverseMatch:
                pass

    def is_empty(self):
        # Make sure the element is rendered.
        return False


class AppIconList(modules.AppList):
    """
    The list of applications, icon style.

    .. image:: /images/appiconlist.png
       :width: 471px
       :height: 124px
       :alt: AppIconList module for django-fluent-dashboard

    It uses the ``FLUENT_DASHBOARD_APP_ICONS`` setting to find application icons.
    """

    #: Specify the template to render
    template = 'fluent_dashboard/modules/app_icon_list.html'

    # Allow old Django 1.2 MEDIA_URL, but prefer STATIC_URL if it's set.
    #: The current static root (considered read only)
    icon_static_root = getattr(settings, 'STATIC_URL', settings.MEDIA_URL) or settings.MEDIA_URL
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

    .. image:: /images/cmsappiconlist.png
       :width: 471px
       :height: 124px
       :alt: CmsAppIconList module for django-fluent-dashboard
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


class CacheStatusGroup(modules.Group):
    """
    Display status modules for Varnish en Memcache, in a :class:`~admin_tools.modules.Group` module.

    This module is only displayed when the :ref:`dashboardmods` package
    is installed, added to the ``INSTALLED_APPS``, and the caches are configured and reachable.
    For more information, see the :ref:`optional dependencies <cachestatus>` page.

    .. image:: /images/cachestatusgroup.png
       :width: 471px
       :height: 198px
       :alt: CacheStatusGroup module for django-fluent-dashboard
    """

    #: The default title
    title = _("System status")
    #: The default display mode, can be "tabs", "stacked" or "accordion"
    display = "accordion"

    def init_with_context(self, context):
        """
        Initializes the status list.
        """
        super(CacheStatusGroup, self).init_with_context(context)

        if 'dashboardmods' in settings.INSTALLED_APPS:
            import dashboardmods
            memcache_mods = dashboardmods.get_memcache_dash_modules()

            try:
                varnish_mods = dashboardmods.get_varnish_dash_modules()
            except (socket.error, KeyError) as e:
                # dashboardmods 2.2 throws KeyError for 'cache_misses' when the Varnish cache is empty.
                # Socket errors are also ignored, to work similar to the memcache stats.
                logger.exception("Unable to request Varnish stats: {0}".format(str(e)))
                varnish_mods = []

            self.children = memcache_mods + varnish_mods
