# -*- coding: utf-8 -*-
"""
Sample Elixir-powered model definition for the repoze.what SQL plugin.

This model definition has been taken from a quickstarted TurboGears 2 project,
but it's absolutely independent of TurboGears.

"""

import os
from hashlib import sha1
from datetime import datetime

from elixir import Entity, Field
from elixir import DateTime, Unicode
from elixir import using_options
from elixir import ManyToMany


class User(Entity):
    """Reasonably basic User definition. Probably would want additional
    attributes.
    """
    using_options(tablename="user", auto_primarykey="user_id")

    user_name = Field(Unicode(16), required=True, unique=True)

    _password = Field(Unicode(80), colname="password", required=True)

    groups = ManyToMany(
        "Group",
        inverse="users",
        tablename="user_group",
        local_colname="group_id",
        remote_colname="user_id",
        )

    def _set_password(self, password):
        """Hash password on the fly."""
        hashed_password = password

        if isinstance(password, unicode):
            password_8bit = password.encode('UTF-8')
        else:
            password_8bit = password
        
        salt = sha1()
        salt.update(os.urandom(60))
        hash = sha1()
        hash.update(password_8bit + salt.hexdigest())
        hashed_password = salt.hexdigest() + hash.hexdigest()

        # Make sure the hased password is an UTF-8 object at the end of the
        # process because SQLAlchemy _wants_ a unicode object for Unicode
        # fields
        if not isinstance(hashed_password, unicode):
            hashed_password = hashed_password.decode('UTF-8')

        self._password = hashed_password

    def _get_password(self):
        """Return the password hashed"""
        return self._password

    password = descriptor=property(_get_password, _set_password)

    def validate_password(self, password):
        """Check the password against existing credentials.

        :param password: the password that was provided by the user to
            try and authenticate. This is the clear text version that we will
            need to match against the hashed one in the database.
        :type password: unicode object.
        :return: Whether the password is valid.
        :rtype: bool
        
        """
        hashed_pass = sha1()
        hashed_pass.update(password + self.password[:40])
        return self.password[40:] == hashed_pass.hexdigest()


class Group(Entity):
    """An ultra-simple group definition."""
    
    using_options(tablename="group", auto_primarykey="group_id")

    group_name = Field(Unicode(16), unique=True)

    display_name = Field(Unicode(255))

    created = Field(DateTime, default=datetime.now)

    users = ManyToMany("User")

    permissions = ManyToMany(
        "Permission",
        inverse="groups",
        tablename="group_permission",
        local_colname="group_id",
        remote_colname="permission_id",
        )


class Permission(Entity):
    """A relationship that determines what each Group can do"""
    
    using_options(tablename="permission", auto_primarykey="permission_id")

    permission_name = Field(Unicode(16), unique=True)

    groups = ManyToMany("Group")
