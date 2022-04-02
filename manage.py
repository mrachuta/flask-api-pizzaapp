"""
This is wrapper used to start application
"""

import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from pizzaapp.config import app_config
from pizzaapp.app import create_app, db


class Migration:

    """
    Class responsible for DB migration process
    """

    def __init__(self, env_name):

        self.env_name = env_name
        self.app = create_app(self.env_name)
        self.manager = Manager(app=self.app)

    def do_migration(self):

        """
        Perform changes in DB
        """

        Migrate(app=self.app, db=db)
        self.manager.add_command("db", MigrateCommand)
        migration.manager.run()


if __name__ == "__main__":

    try:
        migration = Migration(os.environ.get("FLASK_ENV"))
        migration.do_migration()
    except KeyError:
        print("ERROR: set environment with FLASK_ENV")
        print(f"Possible profiles:{' '.join(map(str, app_config.keys()))}")
