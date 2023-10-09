#!/usr/bin/env python3
'''
Module to execute multiple coroutines at the same time with async
'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    '''
    Asychronous function that executes multiple subroutines

    Args:
        n (int): Number of times that wait_random should be spawned
        max_delay (int): Maximum delay
    '''
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
