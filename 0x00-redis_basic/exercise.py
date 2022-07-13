#!/usr/bin/env python3
"""File for exercise in redis"""


import redis
from typing import Callable, Union
from uuid import uuid4


class Cache():
    """Class for cache"""

    def __init__(self):
        """init redis method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in cache"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key
