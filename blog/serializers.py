from config.app import ma
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from blog.models import Article

class ArticleSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Article
        ordered = True

    id = auto_field(dump_only=True)
    created_at = auto_field(dump_only=True)
