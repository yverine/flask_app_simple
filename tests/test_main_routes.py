import unittest
from flask import current_app
from app import create_app

class MainBlueprintTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

    def tearDown(self):
        self.app_context.pop()

    def test_current_app_exists(self):
        with self.app.app_context():
            self.assertIsNotNone(current_app)

if __name__ == '__main__':
    unittest.main()

