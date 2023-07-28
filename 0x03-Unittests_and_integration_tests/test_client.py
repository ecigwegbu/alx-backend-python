#!/usr/bin/env python3
"""Tasks 4-9. Unittests"""
from parameterized import parameterized
from client import GithubOrgClient
import unittest
from unittest.mock import (
    Mock,
    patch,
)
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


class TestGithubOrgClient(unittest.TestCase):
    """Test that GithubOrgClient.org returns the correct value.

    Use @patch as a decorator to make sure get_json is called once with the
    expected argument but make sure it is not executed.

    Use @parameterized.expand as a decorator to parametrize the test with a
    couple of org examples to pass to GithubOrgClient, in this order:

    google
    abc
    Of course, no external HTTP calls should be made."""

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False}),
    ])
    @patch("requests.get")
    def test_org(self, org: str, test_payload: dict, mock_get: Mock):
        """Test that org returns what it is supposed to return"""
        mock = Mock()
        mock.json.return_value = test_payload
        mock_get.return_value = mock
        organ = GithubOrgClient(org)
        result = organ.org
        self.assertEqual(result, test_payload)
