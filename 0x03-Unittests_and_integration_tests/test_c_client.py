# test_client.py

import unittest
from unittest.mock import patch
from c_client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):

    def test_public_repos_with_mocked_url(self):
        # Create an instance of GithubOrgClient
        client_instance = GithubOrgClient()

        # Mock the public_repos_url property using patch.object
        with patch.object(GithubOrgClient, 'public_repos_url', new="https://api.github.com/orgs/myorg/repos"):
            # Call the public_repos method
            result = client_instance.public_repos()

        # Assert that the result is the expected mocked URL value
        self.assertEqual(result, "Public repos URL: https://api.github.com/orgs/myorg/repos")

if __name__ == '__main__':
    unittest.main()
