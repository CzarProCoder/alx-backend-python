#!/usr/bin/env python3
'''
Module that uses async generator to return a list of random floats
'''
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    '''
    Co-routine that returns a list from the floats
    yielded from async_generator function
    '''
    res = [i async for i in async_generator()]
    return res
