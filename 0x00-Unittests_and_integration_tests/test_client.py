#!/usr/bin/env python3
"""Unit tests for Client"""


from client import GithubOrgClient
from parameterized import parameterized
from unittest import TestCase, mock
from unittest.mock import patch, MagicMock


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
