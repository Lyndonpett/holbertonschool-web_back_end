#!/usr/bin/env python3
""" Basic Async Syntax """


import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> int:
    """Async function that waits random time between 0 and max_delay"""
    random: float = uniform(0, max_delay)
    await asyncio.sleep(random)
    return random
