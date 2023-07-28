#!/usr/bin/env python3
import unittest
from unittest.mock import MagicMock

class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        # Define the inner class
        class TestClass:
            def a_property(self):
                return "Hello from TestClass"

        # Create an instance of the inner class
        inner_instance = TestClass()

        # Mock the inner method
        inner_instance.a_property = MagicMock(return_value="Mocked method result")

        # Call the method under test that uses the inner class
        result = self.test_a_property(inner_instance)

        # Assert the result with the mocked value
        self.assertEqual(result, "Mocked method result")

    def test_a_property(self, inner_obj):
        # Do something with the inner object
        return inner_obj.a_property()

if __name__ == '__main__':
    unittest.main()
