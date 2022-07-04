#!/usr/bin/env python3
"""Unit tests for Utils."""


from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """Test access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a"), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b")),
        ({"a": {"b": 2}}, ("b"))
    ])
    def test_access_nested_map_keyerror(self, nested_map, path):
        """Test access_nested_map keyerror"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
