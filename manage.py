#!/usr/bin/env python

import sys
import os
sys.path.pop(0)
sys.path.insert(0, os.getcwd())

from flask_failsafe import failsafe


@failsafe
def create_app():
    from flask_application import app
    return app

from flask.ext.script import Manager, Server

from flask_application.script import ResetDB


from flask.ext.security.script import (CreateUserCommand, AddRoleCommand,
                                       RemoveRoleCommand, ActivateUserCommand,
                                       DeactivateUserCommand)

manager = Manager(create_app)
manager.add_command("runserver", Server())

manager.add_command("reset_db", ResetDB())
manager.add_command('create_user', CreateUserCommand())
manager.add_command('add_role', AddRoleCommand())
manager.add_command('remove_role', RemoveRoleCommand())
manager.add_command('deactivate_user', DeactivateUserCommand())
manager.add_command('activate_user', ActivateUserCommand())

if __name__ == "__main__":
    manager.run()
