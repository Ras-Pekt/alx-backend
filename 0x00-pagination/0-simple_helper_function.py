#!/usr/bin/env python3
"""
a function named that takes two integer arguments page and page_size
and returns a tuple of size two containing a start index and an end index
"""


def index_range(page: int, page_size: int) -> (int, int):
    """
    Args:
        page: int
        page_size: int
    Return:
        Tuple(int, int)
    """
    end_index = page * page_size
    start_index = page_size * (page - 1)
    if page == 1:
        return (0, end_index)
    return (start_index, end_index)
