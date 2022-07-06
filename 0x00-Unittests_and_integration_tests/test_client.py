#!/usr/bin/env python3
"""Unit tests for Client"""


import unittest
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest import TestCase, mock
from unittest.mock import patch, MagicMock, PropertyMock
from urllib.error import HTTPError
from fixtures import *


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method"""
        cls = GithubOrgClient('org_name')
        self.assertEqual(cls.has_license(repo, license_key), expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for public repos method"""

    @classmethod
    def setUpClass(cls):
        """Set up class for integration tests"""
        cls.get_patcher = patch("requests.get", side_effect=HTTPError)

    @classmethod
    def tearDownClass(cls):
        """Teardown for integration tests"""
        cls.get_patcher.stop()
