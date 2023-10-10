#!/usr/bin/env python3
'''
Module containing a coroutine to measure the run time
of another coroutine
'''
import asyncio
from time import perf_counter
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Function to calculate the duration of 4 coroutines
    that run within the same time

    Returns:
        Returns the duration of the runtime as a float
    '''
    start = perf_counter()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    return (perf_counter() - start)
