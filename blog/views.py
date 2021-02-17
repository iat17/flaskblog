import json
from flask import request, Blueprint, jsonify
from .models import Article
from .serializers import article_schema, articles_schema
from config.extensions import db


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