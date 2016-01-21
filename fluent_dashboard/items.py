"""
Additional menu items.
"""
import django
from admin_tools.menu import items
from django.contrib.contenttypes.models import ContentType
from django.core import urlresolvers
from django.core.exceptions import ObjectDoesNotExist
from django.template.defaultfilters import capfirst
from django.utils.translation import ugettext as _
from fluent_dashboard.appgroups import sort_cms_models
from fluent_dashboard.compat import get_meta_model_name
import re

RE_CHANGE_URL = re.compile("(.+)_([^_]+)_change")


class CmsModelList(items.ModelList):
    """
    A custom :class:`~admin_tools.menu.items.ModelList` that displays menu items for each model.
    It has a strong bias towards sorting CMS apps on top.
    """

    def init_with_context(self, context):
        """
        Initialize the menu.
        """
        # Apply the include/exclude patterns:
        listitems = self._visible_models(context['request'])

        # Convert to a similar data structure like the dashboard icons have.
        # This allows sorting the items identically.
        models = [
            { 'name': get_meta_model_name(model._meta),
              'app_name': model._meta.app_label,
              'title': capfirst(model._meta.verbose_name_plural),
              'url': self._get_admin_change_url(model, context)
            }
            for model, perms in listitems if self.is_item_visible(model, perms)
        ]

        # Sort models.
        sort_cms_models(models)

        # Convert to items
        for model in models:
            self.children.append(items.MenuItem(title=model['title'], url=model['url']))

    def is_item_visible(self, model, perms):
        """
        Return whether the model should be displayed in the menu.
        By default it checks for the ``perms['change']`` value; only items with change permission will be displayed.
        This function can be extended to support "view permissions" for example.

        :param model: The model class
        :param perms: The permissions from :func:`ModelAdmin.get_model_perms()<django.contrib.admin.ModelAdmin.get_model_perms>`.
        """
        return perms['change']


class ReturnToSiteItem(items.MenuItem):
    """
    A "Return to site" button for the menu.
    It redirects the user back to the frontend pages.

    By default, it attempts to find the current frontend URL that corresponds
    with the model that's being edited in the admin 'change' page.
    If this is not possible, the default URL (``/``) will be used instead.

    The menu item has a custom ``returntosite`` CSS class to be distinguishable between the other menu items.
    """
    #: Set the default title
    title = _('Return to site')
    #: Set the default URL
    url = '/'
    # Make the item distinguishable between the other menu items
    css_classes = ['returntosite']

    def init_with_context(self, context):
        """
        Find the current URL based on the context.
        It uses :func:`get_edited_object` to find the model,
        and calls ``get_absolute_url()`` to get the frontend URL.
        """
        super(ReturnToSiteItem, self).init_with_context(context)

        # See if the current page is being edited, update URL accordingly.
        edited_model = self.get_edited_object(context['request'])
        if edited_model:
            try:
                url = edited_model.get_absolute_url()
            except (AttributeError, urlresolvers.NoReverseMatch) as e:
                pass
            else:
                if url:
                    self.url = url

    def get_edited_object(self, request):
        """
        Return the object which is currently being edited.
        Returns ``None`` if the match could not be made.
        """
        resolvermatch = urlresolvers.resolve(request.path_info)
        if resolvermatch.namespace == 'admin' and resolvermatch.url_name and resolvermatch.url_name.endswith('_change'):
            # In "appname_modelname_change" view of the admin.
            # Extract the appname and model from the url name.
            # For some custom views, url_name might not be filled in (e.g. django-polymorphic's subclass_view)
            match = RE_CHANGE_URL.match(resolvermatch.url_name)
            if not match:
                return None

            object_id = resolvermatch.args[0]  # Can be string (e.g. a country code as PK).
            return self.get_object_by_natural_key(match.group(1), match.group(2), object_id)
        return None

    def get_object_by_natural_key(self, app_label, model_name, object_id):
        """
        Return a model based on a natural key.
        This is a utility function for :func:`get_edited_object`.
        """
        try:
            model_type = ContentType.objects.get_by_natural_key(app_label, model_name)
        except ContentType.DoesNotExist:
            return None

        # Pointless to fetch the object, if there is no URL to generate
        # Avoid another database query.
        ModelClass = model_type.model_class()
        if not hasattr(ModelClass, 'get_absolute_url'):
            return None

        try:
            return model_type.get_object_for_this_type(pk=object_id)
        except ObjectDoesNotExist:
            return None
