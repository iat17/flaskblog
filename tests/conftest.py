import pytest

from config.app import create_app
from config.extensions import db as _db
from tests.factories import ArticleFactory


@pytest.fixture
def app():
    flask_app = create_app('tests.settings')
    ctx = flask_app.test_request_context()
    ctx.push()

    yield flask_app

    ctx.pop()


@pytest.fixture
def test_client(app):
    yield app.test_client()


@pytest.fixture
def db(app):
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture
def session(db):
    yield db.session


@pytest.fixture
def article_fixt(db):
    article = ArticleFactory()
    db.session.commit()
    return article
