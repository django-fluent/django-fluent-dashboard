"""
Custom menu for ECMS.

To activate the menu add the following to your settings.py::
    ADMIN_TOOLS_MENU = 'ecms_dashboard.menu.EcmsMenu'
"""
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from admin_tools.menu import items, Menu
from admin_tools.utils import get_admin_site_name
from ecms_dashboard.items import CmsModelList, ReturnToSiteItem
from ecms_dashboard.appgroups import get_application_groups


class EcmsMenu(Menu):
    """
    Custom Menu for edoburu.nl admin site.
    """
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children += [
            items.MenuItem(_('Dashboard'), reverse('%s:index' % site_name)),
            items.Bookmarks(),
        ]

        for title, kwargs in get_application_groups():
            self.children.append(CmsModelList(title, **kwargs))

        self.children += [
            ReturnToSiteItem()
        ]
