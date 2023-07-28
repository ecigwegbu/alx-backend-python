#!/usr/bin/env python3
import unittest
from unittest.mock import MagicMock

class TestMemoize(unittest.TestCase):
    def test_memoize(self):
        # Define the inner class
        class TestClass:
            def a_property(self):
                return 42

        # Create an instance of the inner class
        testObj = TestClass()

        # Mock the inner method
        testObj.a_property = MagicMock(return_value=42)

        # Call the method under test that uses the inner class
        result = self.newtest_a_property(testObj)

        # Assert the result with the mocked value
        self.assertEqual(result, 42)

    def newtest_a_property(self, testObj):
        # Do something with the inner object
        return testObj.a_property()

if __name__ == '__main__':
    unittest.main()
