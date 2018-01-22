django-fluent-dashboard
=======================

The ``fluent_dashboard`` module offers a custom admin dashboard, built on top of
django-admin-tools_ (`docs <https://django-admin-tools.readthedocs.io/>`_).

The django-admin-tools_ package provides a default mechanism to replace the standard Django
admin homepage with a widget based dashboard. The ``fluent_dashboard`` module extends this,
by providing additional widgets (called "modules") such as:

* a "icon list" module for the admin homepage.
* a "welcome" module for the admin homepage.
* a configurable module layout for the admin homepage, through ``settings.py``.
* a "return to site" link.
* an optional "cache statistics" module.

Documentation can be found at: https://django-fluent-dashboard.readthedocs.io/

Screenshot
==========

.. image:: https://github.com/edoburu/django-fluent-dashboard/raw/master/docs/images/dashboard.png
   :width: 1030px
   :height: 715px
   :alt: django-fluent-dashboard preview

Installation
============

First install the module, preferably in a virtual environment. It can be installed from PyPI::

    pip install django-fluent-dashboard

Or the current folder can be installed::

    pip install .

Configuration
-------------

Add the following settings to ``settings.py``:

.. code-block:: python

    INSTALLED_APPS += (
        'fluent_dashboard',

        # enable the admin
        'admin_tools',
        'admin_tools.theming',
        'admin_tools.menu',
        'admin_tools.dashboard',
        'django.contrib.admin',
    )

    ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
    ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': (),
            'OPTIONS': {
                'loaders': (
                    ...
                    'admin_tools.template_loaders.Loader',  # Add this line!
                ),
            }
        }
    ]

The ``admin_tools.theming`` and ``admin_tools.menu`` applications are optional.

Add to ``urls.py``:

.. code-block:: python

    urlpatterns += [
        url(r'^admintools/', include('admin_tools.urls')),
    ]

The database tables for ``admin_tools`` can be created afterwards:

.. code-block:: bash

    ./manage.py migrate

Customizing the dashboard
--------------------------

Adding extra icons
------------------

The ``FLUENT_DASHBOARD_APP_ICONS`` setting is a dictionary that allows you to define extra icons
for your own modules, and overwrite default settings. For example:

.. code-block:: python

    FLUENT_DASHBOARD_APP_ICONS = {
        'auth/user': "user.png"
    }

The icon is expected to be 48x48 pixels.
The icon name is treated in 3 different formats:

* Absolute URLs are passed as-is.
* Icon names with a `/` character, are relative to the ``STATIC_URL``.
* Icon names without any path information, are relative to the current theme folder, e.g. `STATIC_URL`/fluent_dashboard/`themename`/

Organizing the application groups
---------------------------------

The ``FLUENT_DASHBOARD_APP_GROUPS`` setting defines which applications are grouped.
For example:

.. code-block:: python

    FLUENT_DASHBOARD_APP_GROUPS = (
        (_('CMS'), {
            'models': (
                'cms.*',
                'pages.*',
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

Details about these options, and additional settings are explained in the documentation_.

Displaying cache status
-----------------------

This application features optional support for the dashboardmods_ package,
which can display cache statistics. It can be installed using::

    pip install dashboardmods

The application requires the cache backends to be configured, for example:

.. code-block:: python

    INSTALLED_APPS += (
        'dashboardmods',
    )

    # Example Memcache configuration:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'KEY_PREFIX': 'mysite.production',
            'LOCATION': '127.0.0.1:11211',
            'TIMEOUT': 24*3600,
        },
    }

    # Optional, example Varnish configuration:
    VARNISH_MANAGEMENT_ADDRS = ('127.0.0.1:6082',)

When a cache is not configured, it will simply not be displayed by the module.


Related applications
--------------------

The following packages provide additional modules,
which can be displayed at the dashboard:

* django-admin-user-stats_ adds graphs to the dashboard, to see the number of registered users in the last month.
* django-admin-tools-stats_ is derived from the previous package, and adds configurable graphs for any model type.
* dashboardmods_ is detected to display cache statistics, but also features a configure RSS feed module.
* django-admin-tools_ should not be forgotten, because it also provides modules for RSS feeds, link lists and tab grouping.

These modules can be integrated by subclassing the ``FluentIndexDashboard`` class,
and point to that module with the ``ADMIN_TOOLS_INDEX_DASHBOARD`` setting.

Contributing
------------

This module is designed to be generic. In case there is anything you didn't like about it,
or think it's not flexible enough, please let us know. We'd love to improve it!

If you have any other valuable contribution, suggestion or idea,
please let us know as well because we will look into it.
Pull requests are welcome too. :-)


.. _documentation: https://django-fluent-dashboard.readthedocs.io/
.. _dashboardmods: https://github.com/callowayproject/dashboardmods
.. _django-admin-tools: https://github.com/django-admin-tools/django-admin-tools
.. _django-admin-tools-stats: https://github.com/Star2Billing/django-admin-tools-stats
.. _django-admin-user-stats: https://github.com/kmike/django-admin-user-stats

