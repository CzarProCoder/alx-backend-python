#!/usr/bin/env python3
'''
Module containing function that returns the sum of mixed values
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    Function that calculates the sum of mixed values
    '''
    return sum(mxd_lst)
