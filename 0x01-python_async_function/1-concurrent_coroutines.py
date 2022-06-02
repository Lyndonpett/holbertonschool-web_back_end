#!/usr/bin/env python3
"""Executing multiple coroutines concurrently."""


from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """takes in 2 int arguments and returns a list of random numbers"""
    taskList = []
    completeList: List[float] = []

    for i in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        taskList.append(task)

    for task in asyncio.as_completed(taskList):
        completed: float = await task
        completeList.append(completed)

    return completeList
