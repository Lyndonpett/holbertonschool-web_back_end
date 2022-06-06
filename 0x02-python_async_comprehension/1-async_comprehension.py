#!/usr/bin/env python3
"""Coroutine called async_comprehension"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """returns a list of random numbers between 1 and 10"""
    return [x async for x in async_generator()]
