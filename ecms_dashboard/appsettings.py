"""
Overview of all settings which can be customized.
"""
from django.conf import settings

ECMS_DASHBOARD_APP_ICONS = getattr(settings, 'ECMS_DASHBOARD_APP_ICONS', {})
