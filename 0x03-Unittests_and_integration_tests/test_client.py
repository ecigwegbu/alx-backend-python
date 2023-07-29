#!/usr/bin/env python3
"""Unittest for Client Module"""

from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Test that GithubOrgClient.org returns the correct value.
    Use patch as a decorator to make sure get_json is called once with the
    expected argument but make sure it is not executed.
    Use parameterized.expand as a decorator to parametrize the test with a
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
