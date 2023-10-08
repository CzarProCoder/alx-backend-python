#!/usr/bin/env python3
'''
Module containing function that returns a callable function
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Function that returns callable function
    '''
    def multiplier_func(number: float) -> float:
        '''
        Function returned by the parent function
        '''
        return multiplier * number

    return multiplier_func
