#!/usr/bin/env python3
import unittest
from unittest.mock import MagicMock

class TestMemoize(unittest.TestCase):
    def test_mock_inner_method(self):
        # Define the inner class
        class InnerClass:
            def inner_method(self):
                return "Hello from InnerClass"

        # Create an instance of the inner class
        testObj = InnerClass()

        # Mock the inner method
        testObj.inner_method = MagicMock(return_value="Mocked method result")

        # Call the method under test that uses the inner class
        result = self.property_tester(testObj)

        # Assert the result with the mocked value
        self.assertEqual(result, "Mocked method result")

    def property_tester(self, inner_obj):
        # Do something with the inner object
        return inner_obj.inner_method()

if __name__ == '__main__':
    unittest.main()
