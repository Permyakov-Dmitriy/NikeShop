from django.test import TestCase, Client


class TestOrders(TestCase):
    def setUp(self):
        self.c = Client()

    def test_response_status_code(self):
        self.assertEqual(self.c.get('/orders/bucket').status_code, 301)

