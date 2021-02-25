from flask import request, Blueprint, abort, jsonify
from .models import Article
from .serializers import ArticleSchema
from config.extensions import db
import datetime

day = 24*60*60

blog_page = Blueprint('blog_page', __name__)

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)

@blog_page.route('/', methods=['POST'])
def add_article():
    json_data = request.get_json()
    data = article_schema.load(json_data)

    new_article = Article(**data)

    db.session.add(new_article)
    db.session.commit()

    result = article_schema.dump(Article.query.get(new_article.id))
    return result

@blog_page.route('/', methods=['GET'])
def get_articles():
    all_articles = Article.query.filter(Article.is_deleted==False).order_by(Article.created_at)
    result = articles_schema.dump(all_articles)
    return jsonify(result)

@blog_page.route('/<id>', methods=['GET'])
def get_article(id):
    article = Article.query.get(id)
    result = article_schema.dump(article)
    if article and article.is_deleted==False:
        return result
    else:
        return abort(404)

@blog_page.route('/<id>', methods=['PUT'])
def update_article(id):
    article = Article.query.get(id)

    json_data = request.get_json()
    article.title = json_data["title"]
    article.description = json_data["description"]
    article.body = json_data["body"]

    if (datetime.datetime.utcnow() - article.created_at).total_seconds() <= day:
        db.session.commit()
        result = article_schema.dump(Article.query.get(article.id))
        return result
    else:
        return abort(400)

@blog_page.route('/<id>', methods=['DELETE'])
def delete_article(id):
    article = Article.query.get(id)
    article.is_deleted = True

    db.session.commit()
    return 'Post deleted'
