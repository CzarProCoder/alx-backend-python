#!/usr/bin/env python3
'''
Module to calculate the length of different type of elements passed as a list
'''

from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    Return the first element of a list or None if the list is empty.

    Args:
        A list containing elements of different types
    '''
    if lst:
        return lst[0]
    else:
        return None
