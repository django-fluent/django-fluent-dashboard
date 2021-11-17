Changelog
=========

Changes in 2.0 (2021-11-17)
---------------------------

* Added Django 4.0 support.
* Dropped Django 1.11 support.
* Dropped Python 2.7 - 3.5 support.


Changes in 1.0.1 (2019-07-15)
-----------------------------

* Fixed crash in ``ReturnToSiteItem`` when visiting the admin password change form.
* Fixed early gettext calls on module loading.
* Fixed wheel package.
* Fixed setup classifiers.
* Fixed building docs.
* Bump django-admin-tools_ to proper minimal version.
* Reformat code with isort and black.


Changes in 1.0 (2018-01-22)
---------------------------

* Added Django 2.0 support.
* Removed Django 1.5 / 1.6 compatibility.
* Removed Python 2.6 support.
* Use new icons from www.flaticon.com

**Backwards incompatible:** The icon defaults have changed to use flat icons.
Please review and update your ``FLUENT_DASHBOARD_APP_ICONS`` settings.
To keep using the old icon theme, add ``FLUENT_DASHBOARD_ICON_THEME = 'oxygen'`` to your settings.


Released as 1.0a1 (2016-05-08)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Use new icons from www.flaticon.com


Changes in version 0.6.1 (2016-01-21)
-------------------------------------

* Fix Python error in ``ReturnToSiteItem`` when custom admin urls have to url name set.


Changes in version 0.6 (2015-12-30)
-----------------------------------

* Added Django 1.9 support
* Dropped Django 1.4 support


Changes in version 0.5.2 (2015-09-02)
-------------------------------------

* Fixed CSS media inclusion for django-admin-tools_ 0.5.x
  Turns out both version need a different layout.


Changes in version 0.5.2 (2015-09-01)
-------------------------------------

* Fixed CSS media inclusion for django-admin-tools_ 0.6


Changes in version 0.5.1
------------------------

* Fixed Python 3 issue
* Added icons for fluentcms-googlemaps_


Changes in version 0.5.0
------------------------

* Added Django 1.8 compatibility
* Fixed Python 3 issue


Changes in version 0.4.0
------------------------

* Allow passing all ``DashboardModule`` kwargs to ``FLUENT_DASHBOARD_APP_GROUPS``.
* Added new Oxygen icons
* Fix assumption that varnish_ is installed because dashboardmods_ is.
* Fix showing disabled application groups in the menu
* Fix 500 error when PK is not an int.
* Fix missing icons for django-fluent-faq_.
* Fix missing icons for django-fluent-comments_.


Changes in version 0.3.6
------------------------

* Fix error when primary keys are not an integer.
* Added more Oxygen icons.


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
.. _django-fluent-comments: https://github.com/edoburu/django-fluent-comments
.. _django-fluent-faq: https://github.com/edoburu/django-fluent-faq
.. _fluentcms-googlemaps: https://github.com/edoburu/fluentcms-googlemaps
.. _dashboardmods: https://github.com/callowayproject/dashboardmods
.. _varnish: https://github.com/justquick/python-varnish_
