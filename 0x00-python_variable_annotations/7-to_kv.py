#!/usr/bin/env python3
"""Type annotation for to_kv function"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """takes string and value and returns a tuple"""
    return (k, v ** 2)
