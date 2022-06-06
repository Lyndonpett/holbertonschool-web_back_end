#!/usr/bin/env python3
"""Coroutine using asyncio.gather"""


from asyncio import gather
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """returns the runtime of the async_comprehension function"""
    start: float = time()
    await gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end: float = time()
    return end - start
