#!/env/usr/bin/python3
"""Type annotation for to_kv function"""


from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """takes string and value and returns a tuple"""
    return (k, v ** 2)
