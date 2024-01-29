#!/usr/bin/env python3
"""
a function named that takes two integer arguments page and page_size
and returns a tuple of size two containing a start index and an end index
"""
import csv
import math
from typing import List


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
    return (0, end_index) if page == 1 else (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        takes two integer arguments page and page_size
        and returns the appropriate page of the dataset
        """
        if isinstance(page, int) and isinstance(page_size, int):
            assert int(page) > 0
            assert int(page_size) > 0

            start, end = index_range(page, page_size)

            if self.__dataset is None:
                with open(self.DATA_FILE) as f:
                    reader = csv.reader(f)
                    dataset = [row for row in reader]
                return dataset[start:end]
            else:
                return self.__dataset[start:end]

            # start, end = index_range(page, page_size)
            # dataset = self.dataset()
            # dataset_rows = []
            # try:
            #     while start < end:
            #         dataset_rows.append(dataset[start])
            #         start += 1
            #     return (dataset_rows)
            # except IndexError:
            #     return []
        else:
            raise AssertionError
