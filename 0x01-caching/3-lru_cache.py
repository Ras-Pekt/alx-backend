#!/usr/bin/python3
"""a caching system module"""
from base_caching import BaseCaching
import time


class LRUCache(BaseCaching):
    """
    a class that inherits from BaseCaching
    and is a caching system with a LRU limit
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
                lru_key = min(self.access_times, key=self.access_times.get)
                print(f"DISCARD: {lru_key}")
                del self.cache_data[lru_key]
                del self.access_times[lru_key]

    def get(self, key):
        """
        Get an item by key from the cache
        """
        if key in self.cache_data.keys():
            self.access_times[key] = time.time()
        return self.cache_data.get(key)
