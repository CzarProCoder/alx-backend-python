#!/usr/bin/env python3
'''
Module containing a function that returns a task
'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    Regular function to return an asyncio.Task

    Args:
        max_delay(int): Maximum Delay
    '''
    return asyncio.create_task(wait_random(max_delay))
