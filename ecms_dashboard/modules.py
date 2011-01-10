"""
Custom modules for the admin dashboard.

This package adds the following classes:

 * AppIconList
 * EcmsAppIconList

These dashboard modules display the application list as icon view.
"""

from admin_tools.dashboard import modules
from django.conf import settings

# Get settings
MEDIA_PREFIX = settings.MEDIA_URL + "ecms_dashboard/oxygen/"

APP_ICONS = {
    'ecms/cmsobject': MEDIA_PREFIX + 'internet-web-browser.png',
    'ecms/cmslayout': MEDIA_PREFIX + 'view-choose.png',
    'ecms/cmssite':   MEDIA_PREFIX + 'preferences-system-network.png',
    'auth/user':  MEDIA_PREFIX + 'system-users.png',
    'auth/group': MEDIA_PREFIX + 'resource-group.png',
    'sites/site': MEDIA_PREFIX + 'applications-internet.png',
}

APP_ICONS.update(getattr(settings, 'ECMS_DASHBOARD_APP_ICONS', {}))

DEFAULT_ICON = MEDIA_PREFIX + 'unknown.png'



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
                    model['icon'] = self.get_icon_for_model(app_name, model_name) or DEFAULT_ICON
                except ValueError:
                    model['icon'] = DEFAULT_ICON

        # put ECMS on top
        self.children.sort(key=lambda a: (0 if a['name'] == 'ecms' else 1, a['title']))


    def get_icon_for_model(self, app_name, model_name):
        """
        Return the icon for the given model.
        """
        key = "%s/%s" % (app_name, model_name)
        return APP_ICONS.get(key, None)


class EcmsAppIconList(AppIconList):
    """
    An icon list of applications, with a strong bias towards sorting ECMS apps.
    """
    ecms_order = {
        'cmsobject': 1,
        'cmslayout': 2,
        'cmssite': 99
    }


    def init_with_context(self, context):
        super(EcmsAppIconList, self).init_with_context(context)
        apps = self.children

        # Add icons
        ecms = [a for a in apps if a['name'] == 'ecms']
        if ecms:
            ecms[0]['models'].sort(key=lambda model: (self.ecms_order.get(model['name'], 90),
                                                      model['title']))

        # put ECMS on top
        self.children.sort(key=lambda a: (0 if a['name'] == 'ecms' else 1, a['title']))


    def get_icon_for_model(self, app_name, model_name):
        """
        Return the icon for the given model.
        """
        key = "%s/%s" % (app_name, model_name)
        return APP_ICONS.get(key, None)
