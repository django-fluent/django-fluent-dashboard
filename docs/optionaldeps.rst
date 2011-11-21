.. _optionaldeps:

Optional dependencies
=====================

The installation of `django-fluent-dasbboard` can be extended with a few modules.

.. _cachestatus:

Cache status
------------

When the :ref:`dashboardmods` package is installed and configured,
the dashboard uses it to display Memcache and Varnish statistics for superusers.

First install the package::

    pip install dashboardmods

An example configurtion looks like:

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

When a cache is not configured, it will simply not be displayed by
the :class:`~fluent_dashboard.modules.CacheStatusGroup` module.

RSS feeds
---------

The RSS feeds configured by the :ref:`dashboardmods` package will also be displayed at the dashboard.
This requires the `feedparser` module. Install it using::

    pip install feedparser

