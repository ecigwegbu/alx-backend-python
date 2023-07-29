#!/usr/bin/env python3
"""Tasks 4-9. Unittests for Client Module"""

from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock


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

    def test_public_repos_url(self):
        """Use patch as a context manager to patch GithubOrgClient.org"""
        resp = {'repos_url': 'https://api.github.com/orgs/google/repos'}
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock,
                   return_value=resp):
            self.assertEqual(GithubOrgClient('Google')._public_repos_url,
                             resp['repos_url'])


if __name__ == '__main__':
    unittest.main()