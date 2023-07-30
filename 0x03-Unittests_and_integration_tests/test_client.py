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
import utils
from utils import (
    access_nested_map,
    get_json,
    memoize,
)
# import json


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

    @patch("client.get_json")
    def test_public_repos(self, mock_get):
        """Useing @patch as a decorator and context manager"""

        google_repos_url = 'https://api.github.com/orgs/google/repos'
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock,
                          return_value=google_repos_url) as mock_repos:

            mock_get.return_value = [{
                'name': 'whatsApp',
                'Platform': 'Android',
                'repos_url': 'https://api.github.com/orgs/google/repos'}, {
                'name': 'instagram',
                'Platform': 'Android',
                'repos_url': 'https://api.github.com/orgs/google/repos'
            }]
            repo_list = ['whatsApp', 'instagram']
            google = GithubOrgClient('Google')

            result = google.public_repos()

            self.assertEqual(result, repo_list)
            mock_repos.assert_called_once()
            mock_get.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Implement TestGithubOrgClient.test_has_license to unit-test
        GithubOrgClient.has_license.i"""

        self.assertEqual(GithubOrgClient.has_license(repo, license_key),
                         expected)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test the public_repos method, using setup and teardown"""
    pass

    def setupClass(self):
        """Setup Class. This code runs before the class is executed"""
        pass

    def tearDownClass():
        """Teardown code executes after the class executes"""
        pass

    def test_public_repos(self):
        """This is used to test the method public_repos"""
        pass

    def test_public_repos_with_license(self):
        """This is used to test the method with license"""
        pass


if __name__ == '__main__':
    unittest.main()
