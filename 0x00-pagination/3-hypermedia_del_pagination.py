#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:100]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        method with two integer arguments
        and returns a dictionary
        """
        data = self.indexed_dataset()
        current_index = 0 if index is None else index

        assert current_index < len(data) and current_index >= 0

        temp_idx = current_index

        data_list = []
        while temp_idx < current_index + page_size:
            data_list.append(data.get(temp_idx))
            temp_idx += 1

        hyper_idx_dict = {}

        hyper_idx_dict["index"] = current_index
        hyper_idx_dict["data"] = data_list
        hyper_idx_dict["page_size"] = page_size
        hyper_idx_dict["next_index"] = current_index + page_size

        return hyper_idx_dict
