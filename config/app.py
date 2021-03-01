import os
from flask import Flask
from marshmallow import ValidationError
from .extensions import db, migrate, ma, basic_auth
from .settings import SQLALCHEMY_DATABASE_URI
from blog import views


def handle_bad_request(e: ValidationError):
    return e.messages, 400


def create_app() -> Flask:
    app = Flask(__name__)
    register_handlers(app)
    register_views(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False
    app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME', 'admin')
    app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD', 'admin')
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    basic_auth.init_app(app)



def register_views(app):
    app.register_blueprint(views.blog_page, url_prefix='/articles')


def register_handlers(app):
    app.register_error_handler(ValidationError, handle_bad_request)
