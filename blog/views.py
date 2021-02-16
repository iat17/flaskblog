from flask import request
from flask import Blueprint

simple_page = Blueprint('simple_page', __name__)


@simple_page.route('/')
def index():
    home = "<h1>Welcome</h1>"
    return home
