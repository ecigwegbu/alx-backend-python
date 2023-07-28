#!/usr/bin/env python3
"""Tasks 0-3. Unittests with Parameterize, mock, memoize, patch"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
import requests  # debug
from functools import wraps  # debug
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Familiarize yourself with the utils.access_nested_map function and
    understand its purpose. Play with it in the Python console to make sure
    you understand.

    In this task you will write the first unit test for
    utils.access_nested_map.

    Create a TestAccessNestedMap class that inherits from unittest.TestCase.

    Implement the TestAccessNestedMap.test_access_nested_map method to test
    that the method returns what it is supposed to.

    Decorate the method with @parameterized.expand to test the function for
    given inputs"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Mapping):
        """Test that utils.access_nested_map returns what it is supposed
        to return"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a"), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'")
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping, path: Sequence,
                                         expected: Mapping):
        """Test that utils.access_nested_map returns what it is supposed
        to return"""
        self.assertRaises(KeyError, msg=expected)


class TestGetJson(unittest.TestCase):
    """Define the TestGetJson(unittest.TestCase) class and implement the
    TestGetJson.test_get_json method to test that utils.get_json returns
    the expected result.

    We don’t want to make any actual external HTTP calls.
    Use unittest.mock.patch to patch requests.get. Make sure it returns a
    Mock object with a json method that returns test_payload which you
    parametrize alongside the test_url that you will pass to get_json with
    the following inputs:

    test_url="http://example.com", test_payload={"payload": True}
    test_url="http://holberton.io", test_payload={"payload": False}
    Test that the mocked get method was called exactly once (per input) with
    test_url as argument.

    Test that the output of get_json is equal to test_payload."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, test_url: str, test_payload: str, mock_get: Mock):
        """Test get_json with patch, parameterize and mock"""
        mock = Mock()
        mock.json.return_value = test_payload
        mock_get.return_value = mock
        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


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
        pass

        @parameterized.expand([
            42,
            42
        ])
        @patch("self.a_method")
        def test_a_property(self, expected: int, mock_get: Mock):
            mock = Mock()
            mock.return_value = expected
            result = self.a_property()
            self.asssertEqual(result, 42)
