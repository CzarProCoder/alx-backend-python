#!/usr/bin/env python3

'''
Module that contains an asychronous generator function
to generate random numbers
'''
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Function to yield a random number between 0 and 10
    after some short periods of sleep

    Returns
        random numbersd between 0 and 10
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
