from flask import Flask
from .config import app_config

# Import of model is necessary
from .models import db, pizza_model
from flask import render_template, url_for
from .views.pizza_view import pizza_api as pizza_blueprint


def create_app(env_name):

    """
    Create app
    """

    app = Flask(__name__, template_folder="templates")

    app.config.from_object(app_config[env_name])
    db.init_app(app)
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
        return render_template("index/index.html", title=index_title, endp=index_endp)

    return app
