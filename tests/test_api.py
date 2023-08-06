import json
from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application
from api import GenerateHandler, DataHandler

class TestGenerateHandler(AsyncHTTPTestCase):
    def get_app(self):
        return Application([(r"/generate", GenerateHandler)])

    def test_post(self):
        response = self.fetch('/generate', method='POST', body=json.dumps({'text': 'Olá Spark!'}))
        self.assertEqual(response.code, 200)
        self.assertIn('generated_text', json.loads(response.body))

class TestDataHandler(AsyncHTTPTestCase):
    def get_app(self):
        return Application([(r"/data/(.*)", DataHandler)])

    def test_get(self):
        response = self.fetch('/data/1', method='GET')
        self.assertEqual(response.code, 200)

    def test_post(self):
        response = self.fetch('/data/1', method='POST', body=json.dumps({'text': 'Olá Kafka!'}))
        self.assertEqual(response.code, 201)

    def test_put(self):
        response = self.fetch('/data/1', method='PUT', body=json.dumps({'text': 'Olá MongoDB!'}))
        self.assertEqual(response.code, 200)

    def test_delete(self):
        response = self.fetch('/data/1', method='DELETE')
        self.assertEqual(response.code, 204)
