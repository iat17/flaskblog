import os

ENV = 'development'
TESTING = True
SQLALCHEMY_DATABASE_URI = 'sqlite://'
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_SORT_KEYS = False
BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME', 'test_user')
BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD', 'test_password')
