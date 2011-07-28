"""
Internal split of applications
"""
from ecms_dashboard import appsettings
import itertools

_groups = [group[1] for group in appsettings.ECMS_DASHBOARD_APP_GROUPS]

ALL_KNOWN_APPS = list(itertools.chain(*_groups))
if '*' in ALL_KNOWN_APPS:
    ALL_KNOWN_APPS.remove('*')  # Default for CMS group, but not useful here.

CMS_APP_NAMES = (
    'cms',    # DjangoCMS
    'pages',  # FeinCMS
    'fiber',  # Django-Fiber
)

CMS_MODEL_ORDER = {
    'page': 1,
    'object': 2,
    'layout': 3,
    'content': 4,
    'file': 5,
    'site': 99
}


def get_application_groups():
    """
    Return the applications of the system, organized in various groups.

    These groups are not connected with the application names,
    but rather with a pattern of applications.
    """

    groups = []
    for title, patterns in appsettings.ECMS_DASHBOARD_APP_GROUPS:
        if '*' in patterns:
            groups += (title, dict(exclude=ALL_KNOWN_APPS, collapsible=False)),
        else:
            groups += (title, dict(models=patterns, collapsible=False)),

    return groups


def sort_cms_models(cms_models):
    cms_models.sort(key=lambda model: (get_cms_model_order(model['name']), model['title']))


def is_cms_app(app_name):
    return app_name in CMS_APP_NAMES or 'cms' in app_name


def get_app_order(app_name):
    if is_cms_app(app_name):
        return 0
    else:
        return 1


def get_cms_model_order(model_name):
    for name, order in CMS_MODEL_ORDER.iteritems():
        if name in model_name:
            return order
    return 99
