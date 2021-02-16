from flask import Flask
from .extensions import db, migrate, ma
from .settings import SQLALCHEMY_DATABASE_URI
from blog import views


def create_app() -> Flask:
    app = Flask(__name__)
    register_views(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)



def register_views(app):
    app.register_blueprint(views.simple_page)
