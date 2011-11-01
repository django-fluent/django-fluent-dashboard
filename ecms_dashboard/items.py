"""
Custom menu items
"""
from admin_tools.menu import items
from django.core import urlresolvers
from django.template.defaultfilters import capfirst
from django.utils.translation import ugettext as _
from ecms_dashboard.appgroups import sort_cms_models

# For now, just allow this package to be used outside the main ECMS module
# Later, this could use a registry or backend system to support other modules.
try:
    from ecms.admin.utils import get_current_edited_page
except ImportError:
    get_current_edited_page = lambda r: None


class CmsModelList(items.ModelList):
    """
    An menu of models, with a strong bias towards sorting CMS apps.
    """
    def init_with_context(self, context):
        listitems = self._visible_models(context['request'])

        # Convert to dictionary items first, like the dashboard icons.
        models = [
            { 'name': model.__name__,
              'title': capfirst(model._meta.verbose_name_plural),
              'url': self._get_admin_change_url(model, context)
            }
            for model, perms in listitems if perms['change']
        ]

        # Sort models.
        sort_cms_models(models)

        # Convert to items
        for model in models:
            self.children.append(items.MenuItem(title=model['title'], url=model['url']))


class ReturnToSiteItem(items.MenuItem):
    """
    A logout button for the menu.
    """
    title = _('Return to site')
    url = '/'
    css_classes = ['ecms-menu-item-tosite']

    def init_with_context(self, context):
        super(ReturnToSiteItem, self).init_with_context(context)

        # See if the current page is being edited, update URL accordingly.
        edited_page = get_current_edited_page(context['request'])
        if edited_page:
            self.url = edited_page.url
