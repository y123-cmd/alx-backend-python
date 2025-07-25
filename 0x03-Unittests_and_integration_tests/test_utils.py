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

if __name__ == "__main__":
    unittest.main()
