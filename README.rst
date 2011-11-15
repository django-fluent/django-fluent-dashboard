Introduction
============


Installation
===========

First install the module, preferably in a virtual environment::

    mkvirtualenv fluent --no-site-packages
    workon fluent
    git clone https://github.com/edoburu/django-fluent-dashboard.git
    cd django-fluent-dashboard
    python setup.py install

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
        url(r'/admintools/', include('admin_tools.urls'))
    )

The database can be created afterwards::

    ./manage.py syncdb

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

