.. _configuration:

Configuration
=============

A quick overvivew of the available settings:

.. code-block:: python

    FLUENT_DASHBOARD_ICON_THEME = 'oxygen'

    FLUENT_DASHBOARD_APP_ICONS = {
        'cms/page': 'internet-web-browser.png',
        'auth/user':  'system-users.png',
        'auth/group': 'resource-group.png',
        'sites/site': 'applications-internet.png',
        'google_analytics/analytics': 'view-statistics.png',
        'registration/registrationprofile': 'list-add-user.png'
        # ...
    }

    FLUENT_DASHBOARD_DEFAULT_ICON = 'unknown.png'

    FLUENT_DASHBOARD_APP_GROUPS = (
        (_('CMS'), (
            '*',
        )),
        (_('Interactivity'), (
            'django.contrib.comments.*',
            'form_designer.*'
            'threadedcomments.*',
            'zinnia.*',
        )),
        (_('Administration'), (
            'django.contrib.auth.*',
            'django.contrib.sites.*',
            'google_analytics.*',
            'registration.*',
        )),
    )

The icon names/paths are parsed in the following way:

* When the icon is an absolute URL, it is used as-is.
* When the icon contains a slash, it is relative from the ``STATIC_URL``.
* When the icon has no slashes, it's relative to the theme url folder (typically `STATIC_URL`/ecms_dashboard/`themename`/),

Full list of settings
---------------------

.. _FLUENT_DASHBOARD_ICON_THEME:

FLUENT_DASHBOARD_ICON_THEME
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The icon theme defines which folder is used to find the icons.
This allows to easily switch between icon sets without having to update all settings.
The current theme is "Oxygen", which is freely available from KDE.
You may use the icons under the `LGPL 3 license <http://www.gnu.org/licenses/lgpl-3.0.html>`_.

FLUENT_DASHBOARD_APP_ICONS
~~~~~~~~~~~~~~~~~~~~~~~~~~

A dictionary of the `app/model`, and the associated icon.
For a few commonly know applications, icons are already provided.
Any key defined in ``settings.py`` overrides the default.

FLUENT_DASHBOARD_DEFAULT_ICON
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case a suitable icon is not found, this icon is used.

FLUENT_DASHBOARD_APP_GROUPS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The application groups to display at the dashboard.
Each tuple defines the title, and list of included modules.
By default, there is a section for "CMS", "Interactivity" and "Administration" filled with known Django applications.

The ``*`` selector without any application name, is special:
it functions as a catch-all for all remaining unmatched items.

