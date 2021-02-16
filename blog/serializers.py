from config.app import ma


class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'body', 'created_at', 'is_deleted')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)