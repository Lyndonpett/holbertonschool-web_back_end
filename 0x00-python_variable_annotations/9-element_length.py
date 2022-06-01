#!/env/usr/bin/python3
"""Type annotations for Python variables."""


from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with the element and its length."""
    return [(element, len(element)) for element in lst]
