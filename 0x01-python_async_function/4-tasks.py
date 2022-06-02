#!/usr/bin/env python3
"""Asyncio Tasks"""


from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """takes in 2 int arguments and returns a list of random numbers"""
    taskList = []
    completeList: List[float] = []

    for i in range(n):
        task = task_wait_random(max_delay)
        taskList.append(task)

    for task in asyncio.as_completed(taskList):
        completed: float = await task
        completeList.append(completed)

    return completeList
