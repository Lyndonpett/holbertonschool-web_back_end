#!/usr/bin/env python3
"""Helper function for pagination"""


def index_range(page, page_size):
    """returns a tuple of size two containing a start index and an end index"""
    if page == 0 and page_size:
        # handles the case where page is 0
        end = page_size
        start = 0
        return start, end

    if page and page_size:
        end = page * page_size
        start = end - page_size
        return start, end
