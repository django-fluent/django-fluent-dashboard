Introduction
============

The ``fluent_dashboard`` module offers a custom admin dashboard, built on top of
`django-admin-tools <https://bitbucket.org/izi/django-admin-tools/wiki/Home>`_ (`docs <http://django-admin-tools.readthedocs.org/>`_).

The `django-admin-tools` provides a default mechanism to replace the standard Django
admin homepage with a widget based dashboard. The ``fluent_dashboard`` module extends this,
by providing additional widgets (called "modules") such as:

* a "icon list" module for the admin homepage.
* a "welcome" module for the admin homepage.
* a configurable module layout for the admin homepage, through ``settings.py``.
* a "return to site" link.

Installation
===========

First install the module, preferably in a virtual environment::

    pip install .

Configuration
-------------

Next, create a project which uses the CMS::

    cd ..
    django-admin.py startproject fluentdemo

It should have the following settings::

    INSTALLED_APPS += (
        'fluent_dashboard',

        # enable the admin
        'admin_tools',     # for staticfiles in Django 1.3
        'admin_tools.theming',
        'admin_tools.menu',
        'admin_tools.dashboard',
        'django.contrib.admin',
    )

    ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
    ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'

Note that some ``admin_tools`` applications are optional,
yet recommended to have the full experience of the module.

In ``urls.py``::

    urlpatterns += patterns('',
        url(r'/admintools/', include('admin_tools.urls')),
    )

The database tables for ``admin_tools`` can be created afterwards::

    ./manage.py syncdb
    ./manage.py migrate    # If South is installed

Customizing the dashboard
--------------------------

The FLUENT_DASHBOARD_APP_ICONS is a dictionary that allows you to define extra icons
for your own modules, and overwrite default settings. For example::

    FLUENT_DASHBOARD_APP_ICONS = {
        'auth/user': "user.png"
    }

The icon is expected to be 48x48 pixels.
The icon name is treated in 3 different formats:

* Absolute URLs are passed as-is.
* Icon names with a `/` character, are relative to the ``STATIC_URL`` (or ``MEDIA_URL`` for Django 1.2).
* Icon names without any path information, are relative to the current theme folder, e.g. `STATIC_URL`/fluent_dashboard/`themename`/

.. seealso::

    More customization options are explained in the documentation.

