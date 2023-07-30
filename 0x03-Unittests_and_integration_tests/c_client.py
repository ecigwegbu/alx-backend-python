# client.py

class GithubOrgClient:
    def __init__(self):
        self._public_repos_url = "https://api.github.com/users/username/repos"

    @property
    def public_repos_url(self):
        return self._public_repos_url

    def public_repos(self):
        # Use the public_repos_url property
        return f"Public repos URL: {self.public_repos_url}"
