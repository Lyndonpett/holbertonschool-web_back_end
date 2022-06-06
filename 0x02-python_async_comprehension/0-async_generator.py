#!/usr/bin/env python3
"""Coroutine async_generator"""


import asyncio
from random import uniform
from typing import Generator



async def async_generator()  -> Generator[float, None, None]:
    """loop 10 times, wait 1 second, yield a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(1, 10)
