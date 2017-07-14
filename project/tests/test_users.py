# project/tests/test_users.py


import json

from project.tests.base import BaseTestCase


class TestService(BaseTestCase):
    """Tests for the Users Service"""

    def test_users(self):
        """Ensure the  /ping route behaves correctly"""
        response = self.client.get('/ping')
        data = json.loads(response.data.decode())
        self.sassertEqual(response.data.decode())
        self.assertIn('pong!', data['message'])
        self.assertIn('success', data['status'])
