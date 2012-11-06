Changes in version 0.3.2
------------------------

* Fix dashboard icons when admin is mounted in a subpath (e.g. ``/en/admin/``)
* Added ``fluent_dashboard/modules/personal_text.html`` template to change the personal text easily.
* Added ``*.UserProfile`` to the Administration group.
* Added various Oxygen icons to assist other projects.


Changes in version 0.3.1
------------------------

* Added ``FLUENT_DASHBOARD_DEFAULT_MODULE`` setting, to switch between ``AppList``,  ``ModelList``, etc..
* Improved support for the ``admin_tools.dashboard.modules.ModelList`` module.


Changes in version 0.3.0
------------------------

* Added *dashboardmods* integration, automatically detected.
* Added icons for *django-fluent-pages*, *django-media-tree* and *django-fluent-blogs*.
* Improved README setup
* Fixed requirements for readthedocs
* Fixed installation problems on Windows


Changes in version 0.2.0
------------------------

First public release

* Renamed app to ``fluent_dashboard``.
* Added icons for ``google_analytics``, Django CMS, FeinCMS, Zinnia, comments, tagging
* Added icon theme switching
* Added documentation
* Added setup files
* Added settings:

 * ``FLUENT_DASHBOARD_CMS_PAGE_MODEL``
 * ``FLUENT_DASHBOARD_CMS_APP_NAMES``
 * ``FLUENT_DASHBOARD_CMS_MODEL_ORDER``

* Improved frontend detection in ``ReturnToSiteItem``
* Changed icon paths to be relative from the ``STATIC_URL``.
* Changed ``FLUENT_DASHBOARD_APP_GROUPS`` items to dictionary layout
* Fixed model name detection when using a subdirectory.
* Fixed sorting in menu.


Version 0.1.0
-------------

Initial internal release
