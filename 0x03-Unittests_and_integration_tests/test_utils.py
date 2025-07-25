#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import unittest
from parameterized import parameterized
from utils import access_nested_map 

class TestAccessNestedMap(unittest.TestCase):
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),  
        ({"a": {"b": 2}}, ("a",), {"b": 2}),  
        ({"a": {"b": 2}}, ("a", "b"), 2),  
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that KeyError is raised with correct message."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Exception message is the missing key (e.g., 'a' or 'b')
        self.assertEqual(str(context.exception), repr(path[len(nested_map)]))

if __name__ == "__main__":
    unittest.main()

