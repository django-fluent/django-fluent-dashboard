"""
Custom dashboards for Django applications.

This package defines the following classes:

* :class:`FluentIndexDashboard`
* :class:`FluentAppIndexDashboard`

These classes need to be linked in ``settings.py`` to be loaded by `django-admin-tools`.
Off course, you can also extend the classes, and use those names in the settings instead.
"""
from distutils.version import LooseVersion
import admin_tools
from admin_tools.dashboard.modules import Group
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard

from fluent_dashboard.modules import PersonalModule, CacheStatusGroup
from fluent_dashboard.appgroups import get_application_groups, get_class


class FluentIndexDashboard(Dashboard):
    """
    A custom home screen for the Django admin interface.

    It displays the application groups based on with :ref:`FLUENT_DASHBOARD_APP_GROUPS` setting.
    To activate the dashboard add the following to your settings.py::

        ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'

    The dashboard modules are instantiated by the following functions, which can be overwritten:

    * :func:`get_personal_module`
    * :func:`get_application_modules`
    * :func:`get_recent_actions_module`
    * :func:`get_rss_modules`
    * :func:`get_cache_status_modules`

    To have a menu which is consistent with the application groups displayed by this module,
    use the :class:`~fluent_dashboard.menu.FluentMenu` class to render the `admin_tools` menu.

    When overwriting this class, the elements can either be added in
    the :func:`__init__` method, or the :func:`init_with_context` method.
    For more information, see the `django-admin-tools` documentation.
    """
    class Media:
        if LooseVersion(admin_tools.VERSION) < LooseVersion('0.6'):
            # Older versions of django-admin-tools used an incorrect format for media.
            css = ("fluent_dashboard/dashboard.css",)
        else:
            css = {
                'all': ("fluent_dashboard/dashboard.css",)
            }

    def __init__(self, **kwargs):
        super(FluentIndexDashboard, self).__init__(**kwargs)
        self.children.append(self.get_personal_module())
        self.children.extend(self.get_application_modules())
        self.children.append(self.get_recent_actions_module())

    def init_with_context(self, context):
        request = context['request']
        if 'dashboardmods' in settings.INSTALLED_APPS:
            self.children.extend(self.get_rss_modules())
            self.children.extend(self.get_cache_status_modules(request))

    def get_personal_module(self):
        """
        Instantiate the :class:`~fluent_dashboard.modules.PersonalModule` for use in the dashboard.
        """
        return PersonalModule(
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
        )

    def get_application_modules(self):
        """
        Instantiate all application modules (i.e.
         :class:`~admin_tools.dashboard.modules.AppList`,
         :class:`~fluent_dashboard.modules.AppIconList` and
         :class:`~fluent_dashboard.modules.CmsAppIconList`)
         for use in the dashboard.
        """
        modules = []
        appgroups = get_application_groups()
        for title, kwargs in appgroups:
            AppListClass = get_class(kwargs.pop('module'))  #e.g. CmsAppIconlist, AppIconlist, Applist
            modules.append(AppListClass(title, **kwargs))
        return modules

    def get_recent_actions_module(self):
        """
        Instantiate the :class:`~admin_tools.dashboard.modules.RecentActions` module for use in the dashboard.
        """
        return modules.RecentActions(_('Recent Actions'), 5, enabled=False, collapsible=False)

    def get_cache_status_modules(self, request):
        """
        Instantiate the :class:`~fluent_dashboard.modules.CacheStatusGroup` module for use in the dashboard.

        This module displays the status of Varnish and Memcache,
        if the :ref:`dashboardmods` package is installed and the caches are configured.
        By default, these modules are only shown for the superuser.
        """
        if not request.user.is_superuser:
            return []

        return [CacheStatusGroup()]

    def get_rss_modules(self):
        """
        Instantiate the RSS modules for use in the dashboard.
        This module displays the RSS feeds of the :ref:`dashboardmods` package, if it is installed, and configured.
        """
        if not 'dashboardmods' in settings.INSTALLED_APPS:
            return []
        import dashboardmods
        return dashboardmods.get_rss_dash_modules()


class FluentAppIndexDashboard(AppIndexDashboard):
    """
    A custom application index page for the Django admin interface.

    This dashboard is displayed when one specific application is opened via the breadcrumb.
    It displays the models and recent actions of the specific application.
    To activate the dashboards add the following to your settings.py::

        ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
    """

    # disable title because its redundant with the model list module
    title = ''

    def __init__(self, app_title, models, **kwargs):
        super(FluentAppIndexDashboard, self).__init__(app_title, models, **kwargs)
        self.children += (
            self.get_model_list_module(),
            self.get_recent_actions_module(),
        )

    def get_model_list_module(self):
        """
        Instantiate a standard :class:`~admin_tools.dashboard.modules.ModelList` class
        to display the models of this application.
        """
        return modules.ModelList(self.app_title, self.models)

    def get_recent_actions_module(self):
        """
        Instantiate the :class:`~admin_tools.dashboard.modules.RecentActions` module
        for use in the appliation index page.
        """
        return modules.RecentActions(
            _('Recent Actions'),
            include_list=self.get_app_content_types(),
            limit=5,
            enabled=False,
            collapsible=False
        )
