#!/usr/bin/env python3
"""Unit tests for Client"""


from client import GithubOrgClient
from parameterized import parameterized
from unittest import TestCase, mock
from unittest.mock import patch, MagicMock, PropertyMock


class TestGithubOrgClient(TestCase):
    """Test for GithubOrgClient"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch("client.get_json",
           MagicMock(return_value={'key': 'value'}))
    def test_org(self, org_name):
        "test org method"
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, {'key': 'value'})

    def test_public_repos_url(self):
        """Test public_repos_url method"""
        with patch("client.get_json",
                   new_callable=PropertyMock,
                   return_value={"repos_url": "url"}):
            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, "url")

    @patch("client.get_json")
    def test_public_repos(self, license):
        """Test public_repos method"""
        with patch('client.GithubOrgClient.public_repos',
                   new_callable=PropertyMock) as mock_repo:
            cls = GithubOrgClient('org_name')
            license.return_value = {'repos_url': 'url'}
            mock_repo.return_value = cls.org.get('repos_url')
            self.assertEqual(cls.public_repos, 'url')
            license.assert_called_once()
            mock_repo.assert_called_once()
