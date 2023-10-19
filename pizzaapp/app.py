"""
This file contains main constructor for app
"""

import os
from flask import Flask
from flask import render_template
from .config import app_config
from flask_migrate import Migrate

# Import of model is necessary
from .models import db
from .views.pizza_view import pizza_api as pizza_blueprint

try: 
    env_name = os.environ["FLASK_ENV"]
    print(f"Running with profile: {env_name}")
except KeyError:
    raise Exception(f"An error occured, set profile with FLASK_ENV environment variable\n" +
                    f"Possible profiles:{' '.join(map(str, app_config.keys()))}")

migrate = Migrate()

def create_app():

    """
    Create app
    """

    app = Flask(__name__, template_folder="templates")

    app.config.from_object(app_config[env_name])
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(pizza_blueprint, url_prefix="/api/v1/pizza")

    @app.route("/", methods=["GET"])
    @app.route("/index", methods=["GET"])
    def index():

        """
        Test endpoint
        """

        index_title = "Welcome page"
        index_endp = [
            # List of endpoints with method (some are filtered out)
            (str(p), ([m for m in p.methods if m not in ("OPTIONS", "HEAD")]))
            for p in app.url_map.iter_rules()
            if str(p).startswith("/api")
        ]
        non_prod = True if os.environ.get('FLASK_ENV') != 'production' else None
        banner_color = os.environ.get('BANNER_COLOR') if non_prod else None
        env_detailed_name = os.environ.get('ENV_DETAILED_NAME') if non_prod else None
        return render_template(
            "index/index.html",
            title=index_title,
            endp=index_endp,
            banner_color=banner_color,
            env_detailed_name=env_detailed_name
        )

    return app
