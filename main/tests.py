from django.test import TestCase, Client
from NikeShop.celery import app
from main.tasks import test

class TestCelery(TestCase):
    def test_task(self):
        test.apply_async()


class TestHome(TestCase):
    def setUp(self):
        self.c = Client()

    def test_response_status_code(self):
        self.assertEqual(self.c.get('').status_code, 200)
        self.assertEqual(self.c.get('/').status_code, 200)
        self.assertEqual(self.c.get('/home').status_code, 404)

    def test_response_template(self):
        self.assertEqual(self.c.get('').templates[0].name, 'main/index.html')
