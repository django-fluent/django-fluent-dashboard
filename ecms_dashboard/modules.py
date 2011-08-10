"""
Custom modules for the admin dashboard.

This package adds the following classes:

 * AppIconList
 * EcmsAppIconList

These dashboard modules display the application list as icon view.
"""
from django.core.urlresolvers import reverse, NoReverseMatch
from django.utils.translation import ugettext as _
from admin_tools.utils import get_admin_site_name
from admin_tools.dashboard import modules
from ecms_dashboard import appsettings
from ecms_dashboard.utils import is_cms_app, sort_cms_models


class PersonalModule(modules.LinkList):
    title = _('Welcome,')
    draggable = False
    deletable = False
    collapsible = False
    template = 'ecms_dashboard/modules/personal.html'

    def init_with_context(self, context):
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
        return False




class AppIconList(modules.AppList):
    """
    The list of applications, icon style.

    It uses the ``ECMS_DASHBOARD_APP_ICONS`` setting to find application icons.
    Icons for the common contrib apps are already defined.
    """
    template = 'ecms_dashboard/modules/app_icon_list.html'

    def init_with_context(self, context):
        super(AppIconList, self).init_with_context(context)
        apps = self.children

        # Add icons
        for app in apps:
            app_name = app['url'].strip('/').split('/')[-1]   # /admin/ecms/
            app['name'] = app_name

            for model in app['models']:
                try:
                    model_name = model['change_url'].strip('/').split('/')[2]   # admin/ecms/cmssite
                    model['name'] = model_name
                    model['icon'] = self.get_icon_for_model(app_name, model_name) or appsettings.ECMS_DASHBOARD_DEFAULT_ICON
                except ValueError:
                    model['icon'] = appsettings.ECMS_DASHBOARD_DEFAULT_ICON

        # put ECMS on top
        self.children.sort(key=lambda a: (0 if a['name'] == 'ecms' else 1, a['title']))


    def get_icon_for_model(self, app_name, model_name):
        """
        Return the icon for the given model.
        """
        key = "%s/%s" % (app_name, model_name)
        return appsettings.ECMS_DASHBOARD_APP_ICONS.get(key, None)


class CmsAppIconList(AppIconList):
    """
    An icon list of applications, with a strong bias towards sorting CMS apps.
    """
    def init_with_context(self, context):
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
