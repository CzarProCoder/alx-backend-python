#!/usr/bin/env python3
'''
Module containing function to calculate the square of a number
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Function to calulate the square of the second value

    Args:
        Float/int: Passed in as the second parameters

    Returns:
        Float: Square of the passed value
    '''
    return k, v**2
