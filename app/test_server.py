import unittest
from server import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to our guest lecture', response.data)

    def test_hello_api(self):
        response = self.app.get('/api')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Hello from the API!"})

if __name__ == '__main__':
    unittest.main()
