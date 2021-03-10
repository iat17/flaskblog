from base64 import b64encode

from flask import Response

from blog.models import Article


def auth():
    credentials = b64encode(b"test_user:test_password").decode('utf-8')
    return {"Authorization": f"Basic {credentials}"}


class TestArticleViews:

    def test_get_articles(self, test_client, article_fixt):
        response: Response = test_client.get('/articles/')
        assert response.status_code == 200
        assert len(response.json) == 1
        article = response.json[0]
        assert article['id'] == article_fixt.id

    def test_get_article(self, test_client, article_fixt):
        response: Response = test_client.get(f'/articles/{article_fixt.id}/')
        assert response.status_code == 200
        article = response.json
        assert article['id'] == article_fixt.id

    def test_create_article(self, test_client, db):
        response: Response = test_client.post('/articles/', headers=auth(), json={
            'title': 'test1',
            'description': 'test1',
            'body': 'test1'
        })

        assert response.status_code == 200

        article = Article.query.first()
        assert article.title == 'test1'

    def test_update_article(self, test_client, article_fixt):
        response: Response = test_client.put(
            f'/articles/{article_fixt.id}/', headers=auth(), json={
                'title': 'test1',
                'description': 'test1',
                'body': 'test1'
            })

        assert response.status_code == 200

        article = Article.query.get(article_fixt.id)
        assert article.title == 'test1'
        assert article.description == 'test1'
        assert article.body == 'test1'

    def test_delete_article(self, test_client, article_fixt):
        response: Response = test_client.delete(
            f'/articles/{article_fixt.id}/', headers=auth())

        assert response.status_code == 200
        assert article_fixt.is_deleted
