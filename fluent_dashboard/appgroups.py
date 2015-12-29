"""
Splitting and organizing applications and models into groups.
This module is mostly meant for internal use.
"""
from fnmatch import fnmatch
from future.utils import iteritems
from django.core.exceptions import ImproperlyConfigured
from fluent_dashboard import appsettings
import itertools

try:
    from importlib import import_module  # Python 2.7+
except ImportError:
    from django.utils.importlib import import_module


_groups = [groupdict['models'] for _, groupdict in appsettings.FLUENT_DASHBOARD_APP_GROUPS]

ALL_KNOWN_APPS = list(itertools.chain(*_groups))
if '*' in ALL_KNOWN_APPS:
    ALL_KNOWN_APPS.remove('*')  # Default for CMS group, but not useful here.

MODULE_ALIASES = {
    'AppList': 'admin_tools.dashboard.modules.AppList',
    'ModelList': 'admin_tools.dashboard.modules.ModelList',
    'AppIconList': 'fluent_dashboard.modules.AppIconList',
    'CmsAppIconList': 'fluent_dashboard.modules.CmsAppIconList',
}


def get_application_groups():
    """
    Return the applications of the system, organized in various groups.

    These groups are not connected with the application names,
    but rather with a pattern of applications.
    """

    groups = []
    for title, groupdict in appsettings.FLUENT_DASHBOARD_APP_GROUPS:
        # Allow to pass all possible arguments to the DashboardModule class.
        module_kwargs = groupdict.copy()

        # However, the 'models' is treated special, to have catch-all support.
        if '*' in groupdict['models']:
            default_module = appsettings.FLUENT_DASHBOARD_DEFAULT_MODULE
            module_kwargs['exclude'] = ALL_KNOWN_APPS + list(module_kwargs.get('exclude', []))
            del module_kwargs['models']
        else:
            default_module = 'CmsAppIconList'

        # Get module to display, can be a alias for known variations.
        module = groupdict.get('module', default_module)
        if module in MODULE_ALIASES:
            module = MODULE_ALIASES[module]
        module_kwargs['module'] = module
        groups.append((title, module_kwargs),)

    return groups


def sort_cms_models(cms_models):
    """
    Sort a set of CMS-related models in a custom (predefined) order.
    """
    cms_models.sort(key=lambda model: (
        get_cms_model_order(model['name']) if is_cms_app(model['app_name']) else 999,
        model['app_name'],
        model['title']
    ))


def is_cms_app(app_name):
    """
    Return whether the given application is a CMS app
    """
    for pat in appsettings.FLUENT_DASHBOARD_CMS_APP_NAMES:
        if fnmatch(app_name, pat):
            return True

    return False


def get_cms_model_order(model_name):
    """
    Return a numeric ordering for a model name.
    """
    for (name, order) in iteritems(appsettings.FLUENT_DASHBOARD_CMS_MODEL_ORDER):
        if name in model_name:
            return order
    return 999


def get_class(import_path):
    """
    Import a class by name.
    """
    # Used from django-form-designer
    # Copyright (c) 2009, Samuel Luescher, BSD licensed

    try:
        dot = import_path.rindex('.')
    except ValueError:
        raise ImproperlyConfigured("{0} isn't a Python path.".format(import_path))

    module, classname = import_path[:dot], import_path[dot + 1:]
    try:
        mod = import_module(module)
    except ImportError as e:
        raise ImproperlyConfigured('Error importing module {0}: "{1}"'.format(module, e))

    try:
        return getattr(mod, classname)
    except AttributeError:
        raise ImproperlyConfigured('Module "{0}" does not define a "{1}" class.'.format(module, classname))
