.. _installation:

Installation
============

This package can be installed using pip:

.. code-block:: sh

    pip install django-fluent-dashboard

This should automatically install `django-admin-tools` 0.4.1 as well.
The 0.4.1 release is required to use Django 1.3.

Django configuration
--------------------

To enable the dashboard in Django, both the `fluent_dashboard` and the `admin_tools` modules have to be added to ``settings.py``:

.. code-block:: python

    INSTALLED_APPS += (
        'fluent_dashboard',

        'admin_tools',     # for staticfiles in Django 1.3
        'admin_tools.theming',
        'admin_tools.menu',
        'admin_tools.dashboard',
        'django.contrib.admin',
    )

.. note::
    The ``admin_tools.theming`` and ``admin_tools.menu`` applications are optional.

Next, the `django-admin-tools` can be configured to use the ``fluent_dashboard`` instead, by using::

    ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
    ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
    ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'
