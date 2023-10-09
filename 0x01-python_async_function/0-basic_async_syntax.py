#!/usr/bin/env python3
'''
Module that waits for a random delay and return it
'''

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
    Asychronous coroutine that returns a random delay

    Args:
        max_delay (int) = Maximum delay to be expected
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return (delay)
