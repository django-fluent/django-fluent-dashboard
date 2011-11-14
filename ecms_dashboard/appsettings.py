"""
Overview of all settings which can be customized.
"""
from django.conf import settings
from django.utils.translation import ugettext as _

ECMS_DASHBOARD_ICON_THEME = getattr(settings, "ECMS_DASHVOARD_ICON_THEME", "oxygen")

# The icon names are not Oxygen specific,
# Oxygen uses the XDG icon naming spec.

ECMS_DASHBOARD_APP_ICONS = {
    'cms/page': 'internet-web-browser.png',
    'snippet/snippet': 'folder-txt.png',
    'filer/folder': 'folder.png',
    'fiber/page': 'internet-web-browser.png',
    'fiber/contentitem': 'folder-txt.png',
    'fiber/image': 'folder-image.png',
    'fiber/file': 'folder.png',
    'ecms/cmsobject': 'internet-web-browser.png',
    'ecms/cmslayout': 'view-choose.png',
    'ecms/cmssite': 'preferences-system-network.png',
    'ecms_media/file': 'folder.png',
    'form_designer/formdefinition': 'mail-mark-task.png',
    'form_designer/formlog': 'view-calendar-journal.png',
    'zinnia/entry': 'view-calendar-journal.png',
    'zinnia/category': 'folder-bookmark.png',
    'comments/comment': 'kde-telepathy.png', #'irc-voice.png',
    'threadedcomments/threadedcomment': 'kde-telepathy.png', #'irc-voice.png',
    'tagging/tag': 'feed-subscribe.png',
    'tagging/taggeditem': 'feed-subscribe.png',
    'auth/user':  'system-users.png',
    'auth/group': 'resource-group.png',
    'google_analytics/analytics': 'view-statistics.png',
    'sites/site': 'applications-internet.png',
    'registration/registrationprofile': 'list-add-user.png'
}

ECMS_DASHBOARD_DEFAULT_ICON = getattr(settings, "ECMS_DASHBOARD_DEFAULT_ICON", 'unknown.png')

ECMS_DASHBOARD_APP_ICONS.update(getattr(settings, 'ECMS_DASHBOARD_APP_ICONS', {}))

ECMS_DASHBOARD_APP_GROUPS = getattr(settings, 'ECMS_DASHBOARD_APP_GROUPS', (
    (_('CMS'), ('*',)),
    (_('Interactivity'), (
        'zinnia.*',
        'django.contrib.comments.*',
        'form_designer.*',
        'threadedcomments.*',
    )),
    (_('Administration'), (
        'django.contrib.auth.*',
        'django.contrib.sites.*',
        'registration.*',
        'google_analytics.*',
    )),
    #(_('Developer tools'), ()),
))
