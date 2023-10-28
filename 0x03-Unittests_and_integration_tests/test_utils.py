#!/usr/bin/env python3
"""Test module for the
utils.py
"""
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from typing import Dict, Union, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """Test casses for the logics of accessing
    the nested map functions
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[Dict, int]
                               ) -> None:
        """tests the nested map function with parameters
        with parameters from parameterized
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict,
                                         path: Tuple[str],
                                         expected: Exception
                                         ) -> None:
        """tests the nested map function with parameters
        with parameters from parameterized
        tests that a KeyError is raised for wrong or invalid arguments
        """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests that get_json returns the expected result
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self,
                      test_url: str,
                      test_payload: Dict,
                      ) -> None:
        """mocks the return value of the requests.get
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('utils.requests.get',
                   return_value=mock_response) as mock_get:
            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """tests the memoization of functions
    """
    def test_memoize(self) -> None:
        """test memoize
        """

        class TestClass:
            """TestClass class
            """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        test_instance = TestClass()
        with patch.object(test_instance,
                          'a_method',
                          return_value=lambda: 42,) as mock_a_method:
            first_result = test_instance.a_property()
            second_result = test_instance.a_property()
            self.assertEqual(first_result, 42)
            self.assertEqual(second_result, 42)
            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
