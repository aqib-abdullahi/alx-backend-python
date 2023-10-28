#!/usr/bin/env python3
"""test client module
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock, PropertyMock
from utils import access_nested_map, get_json, memoize
from typing import Dict, Union, Tuple
import client
from client import GithubOrgClient
GithubOrgClient = __import__('client').GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """tests for the client.GithubOrgClient
    """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    def test_org(self, org: str):
        """tests that the GithubOrgClient.org
        returns the correct value
        """
        with patch('client.get_json',
                   return_value={'org_name': 'TestOrg'}) as mock_get_json:
            client_org = GithubOrgClient(org).org
            called_once_param = GithubOrgClient.ORG_URL.format(org=org)
            mock_get_json.assert_called_once_with(called_once_param)
            self.assertEqual(client_org, {'org_name': 'TestOrg'})

    def test_public_repos_url(self):
        """tests the GithubOrgClient._public_repos_url
        method
        """
        API = 'https://api.github.com/users/abc/repos'
        repos_url_dict = {'repos_url': API}
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock,
                   return_value=repos_url_dict) as mock_org:
            self.assertEqual(GithubOrgClient('abc')._public_repos_url,
                             'https://api.github.com/users/abc/repos')


if __name__ == "__main__":
    unittest.main()
