import json
from flask import request, Blueprint, jsonify, abort
from .models import Article
from .serializers import article_schema, articles_schema
from config.extensions import db
import datetime


simple_page = Blueprint('simple_page', __name__)

@simple_page.route('/create', methods=['POST'])
def add_article():
    title = request.json["title"]
    description = request.json["description"]
    body = request.json["body"]

    new_article = Article(title, description, body)

    db.session.add(new_article)
    db.session.commit()

    return article_schema.jsonify(new_article)

@simple_page.route('/articles', methods=['GET'])
def get_articles():
    all_articles = Article.query.filter(Article.is_deleted==False).order_by(Article.created_at)
    result = articles_schema.dump(all_articles)
    return jsonify(result)

@simple_page.route('/articles/<id>', methods=['GET'])
def get_article(id):
    article = Article.query.get(id)
    if article:
        return article_schema.jsonify(article)
    else:
        return abort(404)

@simple_page.route('/articles/<id>', methods=['PUT'])
def update_article(id):
    article = Article.query.get(id)

    title = request.json["title"]
    description = request.json["description"]
    body = request.json["body"]

    article.title = title
    article.description = description
    article.body = body
    if (datetime.datetime.utcnow() - article.created_at).total_seconds() <= 86400:
        db.session.commit()
        return article_schema.jsonify(article)
    else:
        return abort(400)

@simple_page.route('/articles/delete/<id>', methods=['PUT'])
def delete_article(id):
    article = Article.query.get(id)

    article.is_deleted = True

    db.session.commit()

    return article_schema.jsonify(article)
