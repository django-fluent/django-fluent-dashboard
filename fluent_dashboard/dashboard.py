"""
Custom dashboard for Django applications.

To activate the index dashboard add the following to your settings.py::

    ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'

And to activate the app index dashboard::

    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _

from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard

from fluent_dashboard.modules import CmsAppIconList, PersonalModule
from fluent_dashboard.appgroups import get_application_groups


class FluentIndexDashboard(Dashboard):
    """
    Custom admin dashboard for Django applications.
    """
    class Media:
        css = ("fluent_dashboard/dashboard.css",)

    def init_with_context(self, context):
        quick_links = PersonalModule(
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
        )

        appgroups = get_application_groups()
        recent_actions = modules.RecentActions(_('Recent Actions'), 5, enabled=False, collapsible=False)

        # Add all items
        self.children.append(quick_links)

        for title, kwargs in appgroups:
            self.children.append(CmsAppIconList(title, **kwargs))

        self.children.append(recent_actions)


class FluentAppIndexDashboard(AppIndexDashboard):
    """
    Custom app index dashboard for Django applications.
    """

    # disable title because its redundant with the model list module
    title = ''

    def __init__(self, *args, **kwargs):
        super(FluentAppIndexDashboard, self).__init__(*args, **kwargs)

        model_list = modules.ModelList(self.app_title, self.models)

        recent_actions = modules.RecentActions(
            _('Recent Actions'),
            include_list=self.get_app_content_types(),
            limit=5,
            enabled=False,
            collapsible=False
        )

        self.children += [model_list, recent_actions]


    def init_with_context(self, context):
        """
        Use this method if you need to access the request context.
        """
        return super(FluentAppIndexDashboard, self).init_with_context(context)
