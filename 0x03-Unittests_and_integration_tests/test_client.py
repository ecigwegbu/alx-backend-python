#!/usr/bin/env python3
"""Unittest for Client Module"""

from client import GithubOrgClient
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Test that GithubOrgClient.org returns the correct value.
    Of course, no external HTTP calls should be made."""

    def test_public_repos_url(self):
        """Use patch as a context manager to patch GithubOrgClient.org"""
        resp = {'repos_url': 'https://api.github.com/orgs/google/repos'}
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock,
                   return_value=resp):
            self.assertEqual(GithubOrgClient('Google')._public_repos_url,
                             resp['repos_url'])


if __name__ == '__main__':
    unittest.main()
