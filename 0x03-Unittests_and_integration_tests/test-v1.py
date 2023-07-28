#!/usr/bin/env python3
import unittest
from unittest.mock import MagicMock

class OuterTestClass(unittest.TestCase):
    def test_mock_inner_method(self):
        # Define the inner class
        class InnerClass:
            def inner_method(self):
                return "Hello from InnerClass"

        # Create an instance of the inner class
        inner_instance = InnerClass()

        # Mock the inner method
        inner_instance.inner_method = MagicMock(return_value="Mocked method result")

        # Call the method under test that uses the inner class
        result = self.method_under_test(inner_instance)

        # Assert the result with the mocked value
        self.assertEqual(result, "Mocked method result")

    def method_under_test(self, inner_obj):
        # Do something with the inner object
        return inner_obj.inner_method()

if __name__ == '__main__':
    unittest.main()
