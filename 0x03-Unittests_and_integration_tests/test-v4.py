#!/usr/bin/env python3
import unittest
from unittest.mock import patch
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestMemoize(unittest.TestCase):
    """Test that when calling a_property twice, the correct result is
    returned but a_method is only called once using assert_called_once"""
    def test_memoize(self):
        """Use momoize. Test that when calling a_property twice, the correct
        result is returned but a_method is only called once using
        assert_called_once"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create an instance of TestClass
        testObj = TestClass()

        # Use @patch to mock 'a_method' method of testObj
        with patch.object(testObj, 'a_method', return_value=42) as obj:
            result = testObj.a_property
            result = testObj.a_property
            self.assertEqual(result, 42)
            obj.assert_called_once()


if __name__ == '__main__':
    unittest.main()
