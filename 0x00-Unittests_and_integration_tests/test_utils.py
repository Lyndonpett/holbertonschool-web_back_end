#!/usr/bin/env python3
"""Unit tests for Utils."""


from unittest import TestCase, mock
from parameterized import parameterized
from utils import access_nested_map, get_json


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
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map keyerror"""
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(TestCase):
    """Test get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """Test get_json"""
        with mock.patch("requests.get") as mock_get:
            mock_get.return_value.json.return_value = payload
            self.assertEqual(get_json(url), payload)
