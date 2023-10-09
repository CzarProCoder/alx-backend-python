#!/usr/bin/env python3

'''
Module that measures the duration of the runtime
'''

import asyncio
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Function to measure the average time per number of times
    the function wait_n runs

    Args:
        n(int) : Number of time to run wait random
        max_delay(int): Maximum delay
    '''
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = perf_counter() - start
    return (total_time / n)
