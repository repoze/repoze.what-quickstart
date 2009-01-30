****************************************
The :mod:`repoze.what` Quickstart plugin
****************************************

:Author: Gustavo Narea.
:Status: Official
:Latest release: |release|

.. module:: repoze.what.plugins.quickstart
    :synopsis: Ready-to-use authentication and authorization
.. moduleauthor:: Gustavo Narea <me@gustavonarea.net>

.. topic:: Overview

    Your application may take advantage of a rather simple, and usual, 
    authentication and authorization setup, in which the users' data, the 
    groups and the permissions used in the application are all stored in a 
    SQLAlchemy or Elixir-managed database.


How to install
==============

The minimum requirements are SQLAlchemy, :mod:`repoze.who.plugins.sa`,
:mod:`repoze.what`and :mod:`repoze.what.plugins.sql`, and you can install it 
all with ``easy_install``::
    
    easy_install repoze.what-quickstart

The development mainline is available at the following Subversion repository::

    http://svn.repoze.org/repoze.what/plugins/quickstart/trunk/

How to get help?
================

The prefered place to ask questions is the `Repoze mailing list 
<http://lists.repoze.org/listinfo/repoze-dev>`_ or the `#repoze 
<irc://irc.freenode.net/#repoze>`_ IRC channel. Bugs reports and feature 
requests should be sent to `the issue tracker of the Repoze project 
<http://bugs.repoze.org/>`_.

Contents
========

.. toctree::
    :maxdepth: 2

    Quickstart
    News


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
