from config.extensions import db
from datetime import datetime


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    body = db.Column(db.String(1024), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    is_deleted = db.Column(db.Boolean, default=False)

    def __init__(self, title, description, body):
        self.title = title
        self.description = description
        self.body = body
