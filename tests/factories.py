import factory
from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory

from blog.models import Article
from config.extensions import db


class BaseFactory(SQLAlchemyModelFactory):
    """Base factory."""

    class Meta:
        """Factory configuration."""

        abstract = True
        sqlalchemy_session = db.session


class ArticleFactory(BaseFactory):
    title = Sequence(lambda n: f'article {n}')
    description = Sequence(lambda n: f'article {n}: description')
    body = Sequence(lambda n: f'article {n}: body')

    class Meta:
        model = Article
