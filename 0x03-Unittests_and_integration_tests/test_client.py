#!/usr/bin/env python3
"""test client module
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock, PropertyMock, MagicMock
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        """Tests the GithubOrgClient.public_repos
        method
        """
        test_payload = {
            'repo': [
                {'name': 'Ultimate repository'}
            ]
        }
        mock_get_json.return_value = test_payload['repo']
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock,
                   return_value=test_payload['repo']
                   ) as mock_public_repos_url:
            client_repo = GithubOrgClient('abc').public_repos()
            self.assertEqual(client_repo, ["Ultimate repository"])
            mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repository: Dict,
                         license_key: str,
                         expected: bool) -> bool:
        """tests GithubOrgClient.has_license
        method
        """
        client = GithubOrgClient('abc')
        result = client.has_license(repository, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
