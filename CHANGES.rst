Changes in version 0.3.5
------------------------

* Added filebrowser icon.
* Fix custom user model support of Django 1.5.
* Fix requirements of extras_require cachestatus
* Hide cache status group by default.


Changes in version 0.3.4
------------------------

* Fixed a packaging error, ``dashboard.css`` was missing in the dist.


Changes in version 0.3.3
------------------------

* Added more Oxygen icons.
* Added icon for *sharedcontent* plugin of django-fluent-contents_.
* Fixed ``KeyError`` when a model has add support, but no edit support.
* Fixed icon layout when a model has no permissions to add/edit.
* Fixed welcome text in personal module, remove pages link if the user has no permission to edit pages.
* Bump required version of django-admin-tools_ to 0.5.1, which has Django 1.4/1.5 support.


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


.. _django-admin-tools: https://bitbucket.org/izi/django-admin-tools/wiki/Home
.. _django-fluent-contents: https://github.com/edoburu/django-fluent-contents
