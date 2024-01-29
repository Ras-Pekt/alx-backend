#!/usr/bin/env python3
"""
a module that takes two integer arguments page and page_size
and returns a tuple of size two containing a start index and an end index
"""
import csv
import math
from typing import List, Dict


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
        else:
            raise AssertionError

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        takes two integer arguments page and page_size
        and returns a dictionary
        """
        if not isinstance(page, int) and not isinstance(page_size, int):
            raise AssertionError

        assert int(page) > 0
        assert int(page_size) > 0

        dataset_len = len(self.dataset())
        total_pages = math.ceil(dataset_len / page_size)
        hyper_dict = {}

        hyper_dict["page_size"] = page_size
        hyper_dict["page"] = page
        hyper_dict["data"] = self.get_page(page, page_size)
        hyper_dict["next_page"] = page + 1 if page < total_pages else None
        hyper_dict["prev_page"] = page - 1 if page > 0 else None
        hyper_dict["total_pages"] = total_pages

        return hyper_dict
