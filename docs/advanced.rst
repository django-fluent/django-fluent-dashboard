.. _advanced:

Advanced customization
======================

For advanced dashboard or menu layouts, consider overwriting the classes
provided by the ``admin_tools.dashboard`` and ``fluent_dashboard`` modules.
These can be used in the ``ADMIN_TOOLS_INDEX_DASHBOARD``, ``ADMIN_TOOLS_APP_INDEX_DASHBOARD``, and ``ADMIN_TOOLS_MENU`` settings.
The existing modules in ``fluent_dashboard.modules`` could be reused off course.

The ``fluent_dashboard`` provides the following classes:

:mod:`fluent_dashoard.dashboard`: the custom dashboard classes:

* :class:`fluent_dashboard.dashboard.FluentIndexDashboard`: the dashboard for the homepage.
* :class:`fluent_dashboard.dashboard.FluentAppIndexDashboard``: the dashboard for the application index page.

:mod:`fluent_dashboard.items`: menu icons

* :class:`fluent_dashboard.items.CmsModelList`: a model list, with strong bias of sorting CMS applications on top.
* :class:`fluent_dashboard.items.ReturnToSiteItem`: a custom :class:`admin_tools.menu.items.MenuItem` class, with the "Return to site" link.

:mod:`fluent_dashboard.menu`: the menu classes.

* :class:`fluent_dashboard.menu.FluentMenu`: a custom :class:`admin_tools.menu.Menu` implementation, which honors the ``FLUENT_DASHBOARD_APP_GROUPS`` setting, and adds the `ReturnToSiteItem`.

:mod:`fluent_dashboard.modules`: custom widgets (called "modules") to display at the dashboard.

* :class:`fluent_dashboard.modules.PersonalModule`: a personal welcome text. It displays the ``fluent_dashboard/modules/personal.html`` template.
* :class:`fluent_dashboard.modules.AppIconList`: a :class:`admin_tools.dashboard.modules.AppList` implementation that displays the models as icons.
* :class:`fluent_dashboard.modules.CmsAppIconList`: a `AppIconList` variation with a strong bios towards sorting CMS applications on top.

