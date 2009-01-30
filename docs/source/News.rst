**********************************************
:mod:`repoze.what.plugins.quickstart` releases
**********************************************

This document describes the releases of :mod:`repoze.what.plugins.quickstart`.


.. _1.0rc1:

:mod:`repoze.what.plugins.quickstart` 1.0rc1 (*unreleased*)
===========================================================

This is the first release of :mod:`repoze.what.plugins.quickstart` as an
independent project. This module used to be defined by old versions of
:mod:`repoze.what.plugins.sql`. There are no backwards incompatible changes
at all.

* Introduced the plugin :class:`FriendlyRedirectingFormPlugin
  <repoze.what.plugins.quickstart.FriendlyRedirectingFormPlugin>` and used by
  default in :func:`repoze.what.plugins.quickstart.setup_sql_auth`.
