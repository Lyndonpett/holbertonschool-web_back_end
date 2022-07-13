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

    def get(self, key: str, fn: Callable = None) -> Union[str, int]:
        """Get data from cache"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Get string data from cache"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Get int data from cache"""
        return self.get(key, int)
