#!/usr/bin/env python3
'''
Test script for utils.py
'''
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''
    Test class for utils
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected)
        '''
        Test function for access_nested_map
        '''
        self.assertEqual(access_nested_map(nested_map, path), expected)
