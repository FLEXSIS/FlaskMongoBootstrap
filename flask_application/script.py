from flask.ext.script import Command
from flask_application.models import User, Role, Connection


class ResetDB(Command):
    """Drops all tables and recreates them"""
    def run(self, **kwargs):
        for m in [User, Role, Connection]:
            m.drop_collection()
