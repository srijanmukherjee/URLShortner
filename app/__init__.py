import os
from flask import Flask


def load_config(app: Flask):
    config_object = "config.DevelopmentConfig"

    if os.environ.get("FLASK_ENV") == "production":
        config_object = "config.ProductionConfig"

    app.config.from_object(config_object)


def create_app() -> Flask:
    app = Flask(__name__)

    load_config(app)

    from . import db

    app.teardown_appcontext(db.close_db_client)

    from . import views

    app.register_blueprint(views.bp)

    return app
