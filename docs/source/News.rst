**********************************************
:mod:`repoze.what.plugins.quickstart` releases
**********************************************

This document describes the releases of :mod:`repoze.what.plugins.quickstart`.


Version 1.0.8 (2010-05-20)
==========================

* Made :func:`~repoze.what.plugins.quickstart.setup_sql_auth` skip the default
  :mod:`repoze.who` SQLAlchemy authenticator when requested so with the
  ``use_default_authenticator`` argument.


Version 1.0.7 (2010-05-05)
==========================

* Required :mod:`repoze.who` < 2.0, as v2 is not supported yet.
* Added support for ``skip_authentication`` in the configuration file, by
  Néstor Salceda. ¡Gracias, Néstor!
* Documentation moved to http://what.repoze.org/docs/plugins/quickstart/.


Version 1.0.6 (2010-01-31)
==========================

Added the ability to make :class:`~repoze.who.plugins.friendlyform.FriendlyFormPlugin`
use a character encoding other than the default one (ISO-8859-1/Latin-1).


Version 1.0.5 (2010-01-27)
==========================

Added support for custom ``Max-Age`` values as requested on `pylons-discuss
<http://groups.google.com/group/pylons-discuss/browse_thread/thread/3bf1a87670443b45>`_.
To use it, you can pass the ``cookie_timeout`` and ``cookie_reissue_time``
to :func:`~repoze.what.plugins.quickstart.setup_sql_auth`. This is also supported
in the Ini configuration files.


Version 1.0.4 (2009-12-07)
==========================

Added the options ``log_file`` and ``log_level`` to the ``[authentication]``
section in the :doc:`configuration file <Config>`. Thanks to Darryl Cousins.


Version 1.0.2 and 1.0.3 (2009-10-09)
====================================

Synchronized with the latest version of **repoze.what-pylons**. Thanks to Chris
Perkins.


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
