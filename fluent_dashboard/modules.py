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

from admin_tools.dashboard import modules
from admin_tools.utils import get_admin_site_name
from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.urls import NoReverseMatch, reverse
from django.utils.translation import gettext_lazy as _

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
    title = _("Welcome,")

    #: The model to use for the CMS pages link.
    cms_page_model = appsettings.FLUENT_DASHBOARD_CMS_PAGE_MODEL

    #: Define the template to render
    template = "fluent_dashboard/modules/personal.html"

    def init_with_context(self, context):
        """
        Initializes the link list.
        """
        super().init_with_context(context)
        current_user = context["request"].user
        current_username = current_user.get_short_name() or current_user.get_username()
        site_name = get_admin_site_name(context)

        # Personalize
        self.title = _("Welcome,") + " " + (current_username)

        # Expose links
        self.pages_link = None
        self.pages_title = None
        self.password_link = reverse(f"{site_name}:password_change")
        self.logout_link = reverse(f"{site_name}:logout")

        if self.cms_page_model:
            try:
                app_label, model_name = self.cms_page_model
                model = apps.get_model(app_label, model_name)
                pages_title = model._meta.verbose_name_plural.lower()
                pages_link = reverse(
                    "{site}:{app}_{model}_changelist".format(
                        site=site_name, app=app_label.lower(), model=model_name.lower()
                    )
                )
            except AttributeError:
                raise ImproperlyConfigured(
                    "The value {} of FLUENT_DASHBOARD_CMS_PAGE_MODEL setting (or cms_page_model value) does not reffer to an existing model.".format(
                        self.cms_page_model
                    )
                )
            except NoReverseMatch:
                pass
            else:
                # Also check if the user has permission to view the module.
                # TODO: When there are modules that use Django 1.8's has_module_permission, add the support here.
                permission_name = f"change_{model._meta.model_name.lower()}"

                if current_user.has_perm(f"{model._meta.app_label}.{permission_name}"):
                    self.pages_title = pages_title
                    self.pages_link = pages_link

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
    template = "fluent_dashboard/modules/app_icon_list.html"

    #: The current static root (considered read only)
    icon_static_root = settings.STATIC_URL
    #: The current theme folder (considerd read only)
    icon_theme_root = "{}fluent_dashboard/{}/".format(
        icon_static_root, appsettings.FLUENT_DASHBOARD_ICON_THEME
    )

    def init_with_context(self, context):
        """
        Initializes the icon list.
        """
        super().init_with_context(context)
        apps = self.children

        # Standard model only has a title, change_url and add_url.
        # Restore the app_name and name, so icons can be matched.
        for app in apps:
            app_name = self._get_app_name(app)
            app["name"] = app_name

            for model in app["models"]:
                try:
                    model_name = self._get_model_name(model)
                    model["name"] = model_name
                    model["icon"] = (
                        self.get_icon_for_model(app_name, model_name)
                        or appsettings.FLUENT_DASHBOARD_DEFAULT_ICON
                    )
                except ValueError:
                    model["icon"] = appsettings.FLUENT_DASHBOARD_DEFAULT_ICON

                # Automatically add STATIC_URL before relative icon paths.
                model["icon"] = self.get_icon_url(model["icon"])
                model["app_name"] = app_name

    def _get_app_name(self, appdata):
        """
        Extract the app name from the ``appdata`` that *django-admin-tools* provides.
        """
        return appdata["url"].strip("/").split("/")[-1]  # /foo/admin/appname/

    def _get_model_name(self, modeldata):
        """
        Extract the model name from the ``modeldata`` that *django-admin-tools* provides.
        """
        if "change_url" in modeldata:
            return (
                modeldata["change_url"].strip("/").split("/")[-1]
            )  # /foo/admin/appname/modelname
        elif "add_url" in modeldata:
            return (
                modeldata["add_url"].strip("/").split("/")[-2]
            )  # /foo/admin/appname/modelname/add
        else:
            raise ValueError("Missing attributes in modeldata to find the model name!")

    def get_icon_for_model(self, app_name, model_name, default=None):
        """
        Return the icon for the given model.
        It reads the :ref:`FLUENT_DASHBOARD_APP_ICONS` setting.
        """
        key = f"{app_name}/{model_name}"
        return appsettings.FLUENT_DASHBOARD_APP_ICONS.get(key, default)

    def get_icon_url(self, icon):
        """
        Replaces the "icon name" with a full usable URL.

        * When the icon is an absolute URL, it is used as-is.
        * When the icon contains a slash, it is relative from the ``STATIC_URL``.
        * Otherwise, it's relative to the theme url folder.
        """
        if (
            not icon.startswith("/")
            and not icon.startswith("http://")
            and not icon.startswith("https://")
        ):
            if "/" in icon:
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
        super().init_with_context(context)
        apps = self.children

        cms_apps = [a for a in apps if is_cms_app(a["name"])]
        non_cms_apps = [a for a in apps if a not in cms_apps]

        if cms_apps:
            # Group the models of all CMS apps in one group.
            cms_models = []
            for app in cms_apps:
                cms_models += app["models"]

            sort_cms_models(cms_models)
            single_cms_app = {
                "name": "Modules",
                "title": "Modules",
                "url": "",
                "models": cms_models,
            }

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
    display = "stacked"
    #: Hide by default
    enabled = False

    def init_with_context(self, context):
        """
        Initializes the status list.
        """
        super().init_with_context(context)

        if "dashboardmods" in settings.INSTALLED_APPS:
            import dashboardmods

            memcache_mods = dashboardmods.get_memcache_dash_modules()

            try:
                varnish_mods = dashboardmods.get_varnish_dash_modules()
            except (OSError, KeyError) as e:
                # dashboardmods 2.2 throws KeyError for 'cache_misses' when the Varnish cache is empty.
                # Socket errors are also ignored, to work similar to the memcache stats.
                logger.exception(f"Unable to request Varnish stats: {str(e)}")
                varnish_mods = []
            except ImportError:
                varnish_mods = []

            self.children = memcache_mods + varnish_mods
