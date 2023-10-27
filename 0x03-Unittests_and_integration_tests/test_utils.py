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
    def test_Access_nested_map(self,
                               nested_map: Dict,
                               path: Tuple[str],
                               expected: Union[Dict, int]
                               ) -> None:
        """tests the nested map function with parameters
        with parameters from parameterized
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
