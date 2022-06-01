#!/env/usr/bin/python3
"""Type annotation for sum_mixed_list function"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of all elements in a list"""
    return sum(mxd_lst)
