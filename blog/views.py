from flask import request, Blueprint, jsonify
from blog import models
from blog import serializers


simple_page = Blueprint('simple_page', __name__)

@simple_page.route('/', methods=['GET'])
def index():
    return jsonify({'msg': 'Hi'})
