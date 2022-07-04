#!/usr/bin/env python3
"""Unit tests for Utils."""


from unittest import TestCase, mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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


class TestMemoize(TestCase):
    """Test memoize"""

    def test_memoize(self):
        """Test asserting memoize sets attribute"""

        class TestClass:
            """Test class for memoize"""

            def a_method(self):
                """Test a_method"""
                return 42

            @memoize
            def a_property(self):
                """test a_property"""
                return self.a_method()

        test_object = TestClass()
        test_object.a_method = mock.MagicMock(return_value=42)
        self.assertEqual(test_object.a_property, 42)
        self.assertEqual(test_object.a_property, 42)
        test_object.a_method.assert_called_once()

        with mock.patch.object(TestClass, "a_method",
                               return_value=42) as mock_method:
            test_object2 = TestClass()
            self.assertEqual(test_object2.a_property, 42)
            self.assertEqual(test_object2.a_property, 42)
            mock_method.assert_called_once()
