.. _advanced:

Advanced customization
======================

For advanced dashboard or menu layouts beyond the normal :doc:`settings <configuration>`,
the classes provided by this package (and additionally django-admin-tools_) can be overwritten.

Changing the dashboard layout
-----------------------------

To change the widget layout, extend the :class:`~fluent_dashboard.dashboard.FluentIndexDashboard` class
and create the new module layout in the :func:`~fluent_dashboard.dashboard.FluentIndexDashboard.__init__`
or :func:`~fluent_dashboard.dashboard.FluentIndexDashboard.init_with_context` function.

The custom dashboard class can be loaded by referencing them in either one of these settings:

* ``ADMIN_TOOLS_INDEX_DASHBOARD``
* ``ADMIN_TOOLS_APP_INDEX_DASHBOARD``

Any existing classes from the ``fluent_dashboard.modules`` package could be reused off course.

.. seealso::
    When customizing the dashboard module layout, dont forget to look at the django-admin-tools_
    package and :ref:`other applications <otherapps>` for additional modules to use. These packages have modules for RSS feeds,
    Varnish/Memcache status, and even tabbing/grouping items.

Changing the menu layout
------------------------

The menu layout can be changed by extending the :class:`~fluent_dashboard.menu.FluentMenu` class,
and overwriting the :func:`~fluent_dashboard.menu.FluentMenu.init_with_context` function.

The custom menu class can be loaded by referencing it in the setting:

* ``ADMIN_TOOLS_MENU``

Available classes
-----------------

The `fluent_dashboard` app provides the following classes,
which are suitable for overwriting them:

:mod:`fluent_dashboard.dashboard`: the custom dashboard classes:

* :class:`~fluent_dashboard.dashboard.FluentIndexDashboard`: the dashboard for the homepage.
* :class:`~fluent_dashboard.dashboard.FluentAppIndexDashboard`: the dashboard for the application index page.

:mod:`fluent_dashboard.items`: menu icons

* :class:`~fluent_dashboard.items.CmsModelList`: a model list, with strong bias of sorting CMS applications on top.
* :class:`~fluent_dashboard.items.ReturnToSiteItem`: a custom :class:`~admin_tools.menu.items.MenuItem` class, with the "Return to site" link.

:mod:`fluent_dashboard.menu`: the menu classes.

* :class:`~fluent_dashboard.menu.FluentMenu`: a custom :class:`~admin_tools.menu.Menu` implementation, which honors the ``FLUENT_DASHBOARD_APP_GROUPS`` setting, and adds the :class:`~fluent_dashboard.items.ReturnToSiteItem`.

:mod:`fluent_dashboard.modules`: custom widgets (called "modules") to display at the dashboard.

* :class:`~fluent_dashboard.modules.AppIconList`: an :class:`~admin_tools.dashboard.modules.AppList` implementation that displays the models as icons.
* :class:`~fluent_dashboard.modules.PersonalModule`: a personal welcome text.
* :class:`~fluent_dashboard.modules.CacheStatusGroup`: the statistics of Memcache and Varnish.


.. _django-admin-tools: http://django-admin-tools.readthedocs.org/
