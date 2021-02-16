import json
from flask import request, Blueprint, jsonify
from .models import Article
from blog import serializers


simple_page = Blueprint('simple_page', __name__)

@simple_page.route('/create', methods=['POST'])
def add_artice():
    title = request.json['title']
    description = request.json['description']
    body = request.json['body']
    created_at = request.json['created_at']

    new_article = Article(title, description, body, )
