import unittest

from base_test import BaseTestCase

class TestPages(BaseTestCase):

    def test_home_route(self):
        response = self.client.get("/", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Home", response.data)


if __name__ == "__main__":
    unittest.main()