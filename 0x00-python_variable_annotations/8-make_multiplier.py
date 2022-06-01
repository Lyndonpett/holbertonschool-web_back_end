#!/env/usr/bin/python3
"""Type annotation for make_multiplier function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies its argument by multiplier"""
    def multiplier_func(value: float) -> float:
        """Return the result of multiplying value by multiplier"""
        return value * multiplier
    return multiplier_func
