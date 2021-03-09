from flask import Flask
from marshmallow import ValidationError
from .extensions import db, migrate, ma, basic_auth
from blog import views


def handle_bad_request(e: ValidationError):
    return e.messages, 400


def create_app(config_object='config.settings') -> Flask:
    app = Flask(__name__)
    register_handlers(app)
    register_views(app)
    app.config.from_object(config_object)
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
