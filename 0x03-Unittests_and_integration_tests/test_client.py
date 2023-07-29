#!/usr/bin/env python3
"""Tasks 4-9. Unittests"""
from parameterized import parameterized
from client import GithubOrgClient
import unittest
from unittest.mock import (
    Mock,
    patch,
    PropertyMock
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
    couple of org examples to Pass to GithubOrgClient, in this order:

    google
    abc
    Of course, no external HTTP calls should be made."""

    def test_public_repos_url(self):
        """Use patch as a context manager to patch GithubOrgClient.org and make
        it return a known payload.

        Test that the result of _public_repos_url is the expected one based on
        the mocked payload."""

        testObj = GithubOrgClient("google")
        test_payload = {'repos_url': 'https://example.com'}
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock,
                   return_value=test_payload) as mock2:
            result: Any = testObj._public_repos_url
            self.assertEqual(result, test_payload['repos_url'])
