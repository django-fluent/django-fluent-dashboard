"""
Overview of all settings which can be customized.
"""
from django.conf import settings
from django.utils.translation import ugettext as _

FLUENT_DASHBOARD_ICON_THEME = getattr(settings, "FLUENT_DASHBOARD_ICON_THEME", "flaticons")

# The icon names are somewhat Oxygen specific,
# yet based on the Freedesktop Naming Naming Specification.

if FLUENT_DASHBOARD_ICON_THEME == 'flaticons':
    # New defaults with flaticons
    FLUENT_DASHBOARD_APP_ICONS = {
        'auth/group': 'multiple25.png',
        'auth/user': 'network60.png',
        'comments/comment': 'chat-1.png',
        'filebrowser/filebrowser': 'connectivity2.png',
        'fluent_blogs/entry': 'newspaper1.png',
        'fluent_faq/faqquestion': 'magnifier41.png',
        'fluent_pages/page': 'pencil34.png',
        'fluent_pages/pagelayout': 'layout.png',
        'fluent_comments/fluentcomment': 'chat-1.png',
        'fluentcms_contactform/contactformdata': 'chat.png',
        'fluentcms_googlemaps/marker': 'placeholder8.png',
        'fluentcms_googlemaps/markergroup': 'map35.png',
        'fluentcms_privatenotes/privatenotesitem': 'file.png',
        'redirects/redirect': 'right-arrow7.png',
        'sharedcontent/sharedcontent': 'puzzles3.png',
        'threadedcomments/threadedcomment': 'chat-1.png',
        'sites/site': 'global45.png',
        'users/user': 'network60.png',
    }

    FLUENT_DASHBOARD_DEFAULT_ICON = getattr(settings, "FLUENT_DASHBOARD_DEFAULT_ICON", 'unknown-document.png')
else:
    # Old defaults
    FLUENT_DASHBOARD_APP_ICONS = {
        'auth/group': 'resource-group.png',
        'auth/user':  'system-users.png',
        'cms/page': 'internet-web-browser.png',
        'comments/comment': 'kde-telepathy.png', #'irc-voice.png',
        'dashboardmods/rssdashboardmodule': 'feed-subscribe.png',
        'fluent_blogs/entry': 'view-calendar-journal.png',
        'fluent_pages/pagelayout': 'view-choose.png',
        'fluent_pages/page': 'internet-web-browser.png',
        'fluent_faq/faqquestion': 'system-help.png',
        'fluent_faq/faqcategory': 'custom-bookmarks-help.png',
        'fluent_comments/fluentcomment': 'kde-telepathy.png', #'irc-voice.png',
        'fluentcms_googlemaps/markergroup': 'marble.png',
        'fluentcms_googlemaps/marker': 'preferences-system-session-services.png',
        'fiber/contentitem': 'folder-txt.png',
        'fiber/file': 'folder.png',
        'fiber/image': 'folder-image.png',
        'fiber/page': 'internet-web-browser.png',
        'filebrowser/filebrowser': 'folder.png',
        'filer/folder': 'folder.png',
        'form_designer/formdefinition': 'mail-mark-task.png',
        'form_designer/formlog': 'view-calendar-journal.png',
        'google_analytics/analytics': 'view-statistics.png',
        'page/page': 'internet-web-browser.png',
        'media_tree/filenode': 'folder.png',
        'registration/registrationprofile': 'list-add-user.png',
        'sharedcontent/sharedcontent': 'x-office-document.png',
        'sites/site': 'applications-internet.png',
        'snippet/snippet': 'folder-txt.png',
        'tagging/tag': 'feed-subscribe.png',
        'tagging/taggeditem': 'feed-subscribe.png',
        'threadedcomments/threadedcomment': 'kde-telepathy.png', #'irc-voice.png',
        'zinnia/category': 'folder-bookmark.png',
        'zinnia/entry': 'view-calendar-journal.png',
    }

    FLUENT_DASHBOARD_DEFAULT_ICON = getattr(settings, "FLUENT_DASHBOARD_DEFAULT_ICON", 'unknown.png')

FLUENT_DASHBOARD_CMS_PAGE_MODEL = getattr(settings, "FLUENT_DASHBOARD_CMS_PAGE_MODEL", None)

FLUENT_DASHBOARD_CMS_APP_NAMES = getattr(settings, "FLUENT_DASHBOARD_CMS_APP_NAMES", (
    'cms.*',        # DjangoCMS
    'feincms.*',    # FeinCMS
    'fluent*',      # Fluent pages
    'fiber',        # Django-Fiber
    'filebrowser',  # django-filebrowser
    'media_tree',   # django-media-tree
))

FLUENT_DASHBOARD_CMS_MODEL_ORDER = getattr(settings, "FLUENT_DASHBOARD_CMS_MODEL_ORDER", {
    'page': 1,
    'object': 2,
    'layout': 3,
    'content': 4,
    'file': 5,
    'filebrowser': 5,
    'site': 99
})

FLUENT_DASHBOARD_APP_ICONS.update(getattr(settings, 'FLUENT_DASHBOARD_APP_ICONS', {}))

FLUENT_DASHBOARD_DEFAULT_MODULE = getattr(settings, 'FLUENT_DASHBOARD_DEFAULT_MODULE', 'admin_tools.dashboard.modules.AppList')

FLUENT_DASHBOARD_APP_GROUPS = getattr(settings, 'FLUENT_DASHBOARD_APP_GROUPS', (
    (_('CMS'), {
        'models': [
            "{0}.*".format(app) for app in FLUENT_DASHBOARD_CMS_APP_NAMES
        ],
        'module': 'fluent_dashboard.modules.CmsAppIconList',
        'collapsible': False,
    }),
    (_('Interactivity'), {
        'models': (
            'django.contrib.comments.*',
            'form_designer.*',
            'threadedcomments.*',
            'zinnia.*',
        ),
        'module': 'fluent_dashboard.modules.AppIconList',
        'collapsible': False,
    }),
    (_('Administration'), {
        'models': (
            'django.contrib.auth.*',
            'django.contrib.sites.*',
            '*.UserProfile',
            'registration.*',
            'dashboardmods.*',
            'google_analytics.*',
        ),
        'module': 'fluent_dashboard.modules.AppIconList',
        'collapsible': False,
    }),
    (_('Applications'), {
        'models': ('*',),
        'module': FLUENT_DASHBOARD_DEFAULT_MODULE,
        'collapsible': False,
    }),
    #(_('Developer tools'), ()),
))


# Provide defaults for some popular Django CMSes
if not FLUENT_DASHBOARD_CMS_PAGE_MODEL:
    if 'cms' in settings.INSTALLED_APPS:
        FLUENT_DASHBOARD_CMS_PAGE_MODEL = ('cms', 'page')
    elif 'feincms' in settings.INSTALLED_APPS:
        FLUENT_DASHBOARD_CMS_PAGE_MODEL = ('page', 'page')
    elif 'fluent_pages' in settings.INSTALLED_APPS:
        FLUENT_DASHBOARD_CMS_PAGE_MODEL = ('fluent_pages', 'page')
