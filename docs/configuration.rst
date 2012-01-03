.. _configuration:

Configuration
=============

A quick overvivew of the available settings:

.. code-block:: python

    from django.utils.translation import ugettext_lazy as _


    # Icon settings

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


    # Application grouping:

    FLUENT_DASHBOARD_APP_GROUPS = (
        (_('CMS'), {
            'models': (
                '*cms*.*',
                'fiber.*',
            ),
            'module': 'CmsAppIconList',
            'collapsible': False,
        }),
        (_('Interactivity'), {
            'models': (
                'django.contrib.comments.*',
                'form_designer.*'
                'threadedcomments.*',
                'zinnia.*',
            ),
        }),
        (_('Administration'), {
            'models': (
                'django.contrib.auth.*',
                'django.contrib.sites.*',
                'google_analytics.*',
                'registration.*',
            ),
        }),
        (_('Applications'), {
            'models': ('*',),
            'module': 'AppList',
            'collapsible': True,
        }),
    )


    # CMS integration:

    FLUENT_DASHBOARD_CMS_PAGE_MODEL = ('cms', 'page')

    FLUENT_DASHBOARD_CMS_APP_NAMES = (
        '*cms*',  # wildcard match; DjangoCMS, FeinCMS
        'fiber',  # Django-Fiber
    )

    FLUENT_DASHBOARD_CMS_MODEL_ORDER = {
        'page': 1,
        'object': 2,
        'layout': 3,
        'content': 4,
        'file': 5,
        'site': 99
    }

The icon names/paths are parsed in the following way:

* When the icon is an absolute URL, it is used as-is.
* When the icon contains a slash, it is relative from the ``STATIC_URL``.
* When the icon has no slashes, it's relative to the theme url folder (typically `STATIC_URL`/ecms_dashboard/`themename`/),

Icon settings
-------------

.. _FLUENT_DASHBOARD_ICON_THEME:

FLUENT_DASHBOARD_ICON_THEME
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The icon theme defines which folder is used to find the icons.
This allows to easily switch between icon sets without having to update all settings.
The current theme is "Oxygen", which is freely available from KDE.
You may use the icons under the `LGPL 3 license <http://www.gnu.org/licenses/lgpl-3.0.html>`_.

.. _FLUENT_DASHBOARD_APP_ICONS:

FLUENT_DASHBOARD_APP_ICONS
~~~~~~~~~~~~~~~~~~~~~~~~~~

A dictionary of the `app/model`, and the associated icon.
For a few commonly know applications, icons are already provided.
Any key defined in ``settings.py`` overrides the default.

FLUENT_DASHBOARD_DEFAULT_ICON
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In case a suitable icon is not found, this icon is used.


Application grouping
--------------------

.. _FLUENT_DASHBOARD_APP_GROUPS:

FLUENT_DASHBOARD_APP_GROUPS
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The application groups to display at the dashboard.
Each tuple has a title, and dictionary which can have the following fields:

* **models:** which models should be included. Simple pattern based filtering is provided by :func:`fnmatch()`.
* **collapsible:** whether the group can be collapsed to a single line. Default is ``False`` for all elements to reduce clutter.
* **module:** which dashboard module can be used. Possible values are:

 * :class:`~admin_tools.dashboard.modules.AppList` (the default from `django-admin-tools`).
 * :class:`~fluent_dashboard.modules.AppIconList`
 * :class:`~fluent_dashboard.modules.CmsAppIconList`
 * any other class, specified as full ``module.ClassName`` syntax.

By default, there is a section for "CMS", "Interactivity" and "Administration" filled with known Django applications.

The ``*`` selector without any application name, is special:
it matches all applications which are not placed in any other groups.

CMS integration
---------------

.. _FLUENT_DASHBOARD_CMS_PAGE_MODEL:

FLUENT_DASHBOARD_CMS_PAGE_MODEL
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The model used to display a link to the CMS pages.
The value is a tuple of `application name`, and `model name`.
This is used in the welcome text of the :class:`~fluent_dashboard.modules.PersonalModule`.
For some known CMS applications, this value is already set to a sane default.

FLUENT_DASHBOARD_CMS_APP_NAMES
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A list of patterns to define which applications should be considered as "CMS" applications.
These applications are sorted on top in the :class:`~fluent_dashboard.modules.CmsAppIconList`
and :class:`~fluent_dashboard.items.CmsModelList` classes. The default ``FLUENT_DASHBOARD_APP_GROUPS``
also uses this setting to fill the "CMS" category.

FLUENT_DASHBOARD_CMS_MODEL_ORDER
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A dictionary of `modelname`: `ordering` items, to sort the models of CMS applications in a custom order.
This can be used for example, to display the pages model first, and the files/images models next.
