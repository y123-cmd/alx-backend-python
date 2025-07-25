#!/usr/bin/env python3

"""
Unit tests for utility functions defined in utils.py.

This module contains unittests for:
- access_nested_map
- get_json
- memoize
"""


import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any, Tuple, Dict
from utils import (
    access_nested_map,
    get_json,
    memoize,
)

from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """TestCase for the access_nested_map utility function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping[str, Any],
                               path: Sequence[str],
                               expected: Any) -> None:
        """Test access_nested_map returns correct value for given path."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping[str, Any],
                                         path: Sequence[str]) -> None:
        """Test access_nested_map raises KeyError with invalid path."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """TestCase for the get_json utility function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self,
                      test_url: str,
                      test_payload: Dict[str, Any],
                      mock_get: Mock) -> None:
        """Test get_json returns correct JSON from mocked GET request."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """TestCase for the memoize decorator."""

    def test_memoize(self):
        """Test that memoize caches method results."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
            TestClass, 'a_method', return_value=42
        ) as mock_method:
            test_instance = TestClass()
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
