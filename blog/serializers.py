from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from blog.models import Article


class ArticleSchema(SQLAlchemyAutoSchema):
    id = auto_field(dump_only=True)
    created_at = auto_field(dump_only=True)

    class Meta:
        model = Article
        exclude = ('is_deleted',)
        ordered = True
