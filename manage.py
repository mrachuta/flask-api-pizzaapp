import os
from flask_script import Manager
from pizzaapp.config import app_config
from pizzaapp.app import create_app, db
from flask_migrate import Migrate, MigrateCommand


class Migration:
    def __init__(self, env_name):

        self.env_name = env_name

    def do_migration(self):

        app = create_app(self.env_name)

        migrate = Migrate(app=app, db=db)
        self.manager = Manager(app=app)
        self.manager.add_command("db", MigrateCommand)
        migration.manager.run()


if __name__ == "__main__":

    try:
        migration = Migration(os.environ.get("FLASK_ENV"))
        migration.do_migration()
    except KeyError:
        print("ERROR: set environment with FLASK_ENV")
        print(f"Possible profiles:{' '.join(map(str, app_config.keys()))}")
