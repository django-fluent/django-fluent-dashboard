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
