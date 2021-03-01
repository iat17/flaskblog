from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_basicauth import BasicAuth

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
basic_auth = BasicAuth()
