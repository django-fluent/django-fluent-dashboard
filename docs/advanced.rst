.. _advanced:

Advanced customization
======================

For advanced dashboard or menu layouts, the classes
provided by `django-admin-tools` and `fluent-dashboard` can be overwritten.
These custom classes can be used in the setings:

* ``ADMIN_TOOLS_INDEX_DASHBOARD``
* ``ADMIN_TOOLS_APP_INDEX_DASHBOARD``
* ``ADMIN_TOOLS_MENU``

The existing modules in ``fluent_dashboard.modules`` could be reused off course.


.. seealso::
    When customizing the dashboard module layout, dont forget to look at the `django-admin-tools <http://django-admin-tools.readthedocs.org/>`_
    package and :ref:`other applications <otherapps>` for additional modules to use. These packages have modules for RSS feeds,
    Varnish/Memcache status, and even tabbing/grouping items.

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
* :class:`~fluent_dashboard.modules.CmsAppIconList`: an :class:`~fluent_dashboard.modules.AppIconList` variation with a strong bios towards sorting CMS applications on top.
* :class:`~fluent_dashboard.modules.PersonalModule`: a personal welcome text.

