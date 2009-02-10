**********************************************
:mod:`repoze.what.plugins.quickstart` releases
**********************************************

This document describes the releases of :mod:`repoze.what.plugins.quickstart`.


.. _1.0rc2:

:mod:`repoze.what.plugins.quickstart` 1.0rc2 (2009-02-11)
=========================================================


* :class:`FriendlyRedirectingFormPlugin
  <repoze.what.plugins.quickstart.FriendlyRedirectingFormPlugin>` ignored
  ``environ['SCRIPT_NAME']``.
* Small fixes in the documentation.


.. _1.0rc1:

:mod:`repoze.what.plugins.quickstart` 1.0rc1 (2009-01-30)
=========================================================

This is the first release of :mod:`repoze.what.plugins.quickstart` as an
independent project. This module used to be defined by old versions of
:mod:`repoze.what.plugins.sql`. There are no backwards incompatible changes
at all.

* Introduced the plugin :class:`FriendlyRedirectingFormPlugin
  <repoze.what.plugins.quickstart.FriendlyRedirectingFormPlugin>` and used by
  default in :func:`repoze.what.plugins.quickstart.setup_sql_auth`.
