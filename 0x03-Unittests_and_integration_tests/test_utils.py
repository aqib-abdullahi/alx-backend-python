#!/usr/bin/env python3
"""Test module for the
utils.py
"""
from parameterized import parameterized
import unittest
from utils import access_nested_map
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
        # self.assertEqual(access_nested_map(nested_map, path), expected)
        # self.assertRaises(self, KeyError, access_nested_map(nested_map, path), expected)
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


if __name__ == "__main__":
    unittest.main()
