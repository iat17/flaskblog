import os

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@postgres:5432/postgres')  # 'postgres://postgres:postgres@localhost:5400/postgres'
SQLALCHEMY_TRACK_MODIFICATIONS = False
JSON_SORT_KEYS = False
BASIC_AUTH_USERNAME = os.environ.get('BASIC_AUTH_USERNAME', 'admin')
BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD', 'admin')
