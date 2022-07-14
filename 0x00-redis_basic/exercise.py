#!/usr/bin/env python3
"""File for exercise in redis"""


import redis
from typing import Callable, Union
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Count the number of calls to a method"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args) -> Union[int, str]:
        """Wrapper to increment counter"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Store the call history of a method"""

    @wraps(method)
    def wrapper(self, *args) -> Union[int, str]:
        """Wrapper to store call history"""
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", str(args))
        output = method(self, *args)
        self._redis.rpush(f"{key}:outputs", output)
        return output

    return wrapper


def replay(method: Callable) -> None:
    """Displays history of method calls"""
    locRedis = redis.Redis()
    qual = method.__qualname__

    # get range of inputs and outputs
    inputs = locRedis.lrange(f"{qual}:inputs", 0, -1)
    outputs = locRedis.lrange(f"{qual}:outputs", 0, -1)
    print(f"{qual} was called {len(inputs)} times:")

    # use zip to pair inputs and outputs
    for i, o in zip(inputs, outputs):
        # print input and output and decode to string
        print(f"{qual}(*{(i).decode('utf-8')}) -> {(o).decode('utf-8')}")


class Cache():
    """Class for cache"""

    def __init__(self):
        """init redis method"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
