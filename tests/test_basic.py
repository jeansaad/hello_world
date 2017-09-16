from hello_world import hello_world

from unittest import TestCase


class BasicTest(TestCase):
    def test_basic_hello_world(self):
        """
        Test basic hello world messaging
        """
        self.assertEqual(hello_world(), 'Hello, World!')
