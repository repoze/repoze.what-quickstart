**********************************************
:mod:`repoze.what.plugins.quickstart` releases
**********************************************

This document describes the releases of :mod:`repoze.what.plugins.quickstart`.


Version 1.0.1 (2009-08-14)
==========================

* Added support for :doc:`configuration files <Config>`.
* Added a warning to encourage people to set a custom key to encrypt and decrypt
  the cookies.


Version 1.0 (2009-03-02)
========================

The final version 1.0 of :mod:`repoze.what.plugins.quickstart` is the same as
v1.0rc4, since no bug has been found.


Version 1.0rc4 (2009-02-18)
===========================

* Made the groups/permissions-based authorization pattern optional, as in
  :mod:`repoze.what` itself. If you don't want to use it, set ``group_class``
  and ``permission_class`` to ``None`` (when calling
  :func:`repoze.what.plugins.quickstart.setup_sql_auth`).


Version 1.0rc3 (2009-02-17)
===========================

* Updated the sample SQLAlchemy and Elixir models in the documentation, making
  clear how the SQLAlchemy session object should be imported depending on the
  used framework (if any).
* Moved :class:`repoze.what.plugins.quickstart.FriendlyRedirectingFormPlugin`
  to :class:`repoze.who.plugins.friendlyform.FriendlyFormPlugin`. **This may
  seem like a backwards-incompatible change, but it is not** because since this
  :mod:`repoze.who` plugin was defined in this package as of version 1.0rc1,
  it was recommended not to use it directly because it was a temporary
  location. If you didn't use it directly, you have nothing to worry about.


Version 1.0rc2 (2009-02-11)
===========================


* :class:`FriendlyRedirectingFormPlugin
  <repoze.what.plugins.quickstart.FriendlyRedirectingFormPlugin>` ignored
  ``environ['SCRIPT_NAME']``.
* Small fixes in the documentation.


Version 1.0rc1 (2009-01-30)
===========================

This is the first release of :mod:`repoze.what.plugins.quickstart` as an
independent project. This module used to be defined by old versions of
:mod:`repoze.what.plugins.sql`. There are no backwards incompatible changes
at all.

* Introduced the plugin :class:`FriendlyRedirectingFormPlugin
  <repoze.what.plugins.quickstart.FriendlyRedirectingFormPlugin>` and used by
  default in :func:`repoze.what.plugins.quickstart.setup_sql_auth`.
