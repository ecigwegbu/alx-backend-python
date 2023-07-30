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
import json


class TestGithubOrgClient(unittest.TestCase):
    """Test that GithubOrgClient.org returns the correct value.

    Use @patch as a decorator to make sure get_json is called once with the
    expected argument but make sure it is not executed.

    Use @parameterized.expand as a decorator to parametrize the test with a
    couple of org examples to Pass to GithubOrgClient, in this order:

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

    @patch("utils.get_json")
    def test_public_repos(self, mock_get: Mock):
        """Useing @patch as a decorator and context manager"""

        google_public_repos = ['truth', 'ruby-openid-apps-discovery']
        mock_get.return_value = google_public_repos

        google = GithubOrgClient('Google')
        google_repos_url = 'https://api.github.com/orgs/google/repos'
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock,
                   return_value=google_repos_url) as mock_repos:
            public_repos = google.public_repos()

            print("\nPublic Repos: _____", public_repos)
            print("\ngoogle_public_repos: _____", google_public_repos)
            # self.assertEqual(public_repos, google_public_repos)
            # mock_get.assert_called_once()
            # mock_repos.assert_called_once()
            

if __name__ == '__main__':
    unittest.main()
