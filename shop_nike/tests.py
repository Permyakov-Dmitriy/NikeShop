from django.test import TestCase, Client

class TestShop(TestCase):
    def setUp(self):
        self.c = Client()

    def test_response_status_code(self):
        gender = ['men', 'women', 'baby']
        
        for g in gender:
            self.assertEqual(self.c.get(f'/shop/?gender={g}').status_code, 200)

