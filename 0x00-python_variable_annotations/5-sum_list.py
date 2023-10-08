#!/usr/bin/env python3
'''
Module containing function tha adds a list of float values
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Function to calculate the sum of values passed in a list
    '''
    if input_list is None:
        return 0
    return sum(input_list)
