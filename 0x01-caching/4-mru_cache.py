#!/usr/bin/python3
"""a caching system module"""
from base_caching import BaseCaching
import time


class MRUCache(BaseCaching):
    """
    a class that inherits from BaseCaching
    and is a caching system with a MRU limit
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.access_times = {}

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            self.access_times[key] = time.time()

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru_key = sorted(
                    self.access_times.items(),
                    key=lambda item: item[1],
                    reverse=True
                )
                print(f"DISCARD: {mru_key[1][0]}")
                del self.cache_data[mru_key[1][0]]
                del self.access_times[mru_key[1][0]]

    def get(self, key):
        """
        Get an item by key from the cache
        """
        if key in self.cache_data.keys():
            self.access_times[key] = time.time()
        return self.cache_data.get(key)
