"""
Overview of all settings which can be customized.
"""
from django.conf import settings
from django.utils.translation import ugettext as _

# Allow old Django 1.2 MEDIA_URL, but prefer STATIC_URL if it's set.
MEDIA_PREFIX = getattr(settings, 'STATIC_URL', settings.MEDIA_URL) + "ecms_dashboard/oxygen/"

ECMS_DASHBOARD_APP_ICONS = {
    'cms/page': MEDIA_PREFIX + 'internet-web-browser.png',
    'snippet/snippet': MEDIA_PREFIX + 'folder-txt.png',
    'filer/folder': MEDIA_PREFIX + 'folder.png',
    'fiber/page': MEDIA_PREFIX + 'internet-web-browser.png',
    'fiber/contentitem': MEDIA_PREFIX + 'folder-txt.png',
    'fiber/image': MEDIA_PREFIX + 'folder-image.png',
    'fiber/file': MEDIA_PREFIX + 'folder.png',
    'ecms/cmsobject': MEDIA_PREFIX + 'internet-web-browser.png',
    'ecms/cmslayout': MEDIA_PREFIX + 'view-choose.png',
    'ecms/cmssite':   MEDIA_PREFIX + 'preferences-system-network.png',
    'ecms_media/file': MEDIA_PREFIX + 'folder.png',
    'form_designer/formdefinition': MEDIA_PREFIX + 'mail-mark-task.png',
    'form_designer/formlog': MEDIA_PREFIX + 'view-calendar-journal.png',
    'zinnia/entry': MEDIA_PREFIX + 'view-calendar-journal.png',
    'zinnia/category': MEDIA_PREFIX + 'folder-bookmark.png',
    'comments/comment': MEDIA_PREFIX + 'kde-telepathy.png', #'irc-voice.png',
    'tagging/tag': MEDIA_PREFIX + 'feed-subscribe.png',
    'tagging/taggeditem': MEDIA_PREFIX + 'feed-subscribe.png',
    'auth/user':  MEDIA_PREFIX + 'system-users.png',
    'auth/group': MEDIA_PREFIX + 'resource-group.png',
    'google_analytics/analytics': MEDIA_PREFIX + 'view-statistics.png',
    'sites/site': MEDIA_PREFIX + 'applications-internet.png',
    'registration/registrationprofile': MEDIA_PREFIX + 'list-add-user.png'
}

ECMS_DASHBOARD_DEFAULT_ICON = MEDIA_PREFIX + 'unknown.png'


ECMS_DASHBOARD_APP_ICONS.update(getattr(settings, 'ECMS_DASHBOARD_APP_ICONS', {}))

ECMS_DASHBOARD_APP_GROUPS = getattr(settings, 'ECMS_DASHBOARD_APP_GROUPS', (
    (_('CMS'), ('*',)),
    (_('Interactivity'), ('zinnia.*', 'django.contrib.comments.*', 'form_designer.*')),
    (_('Administration'), ('django.contrib.auth.*', 'django.contrib.sites.*', 'registration.*', 'google_analytics.*',)),
    #(_('Developer tools'), ()),
))
