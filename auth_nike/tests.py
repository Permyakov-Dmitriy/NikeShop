from django.test import TestCase, Client


class TestAuth(TestCase):
    def setUp(self):
        self.c = Client()

    def test_registartion_response_status_code(self):
        self.assertEqual(self.c.get('/registration/').status_code, 200)

    def test_login_response_status_code(self):
        self.assertEqual(self.c.get('/auth/').status_code, 200)

