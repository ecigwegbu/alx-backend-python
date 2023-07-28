#!/usr/bin/env python3
"""0. Parameterize a unit test"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
# import requests
# from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
from utils import access_nested_map, get_json, memoize


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
        # ("One", {}, ("a"), 1),
        ({}, ("a"), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'")
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping, path: Sequence,
                                         expected: Mapping):
        """Test that utils.access_nested_map returns what it is supposed
        to return"""
        self.assertRaises(KeyError, msg=expected)
