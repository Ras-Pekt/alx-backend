#!/usr/bin/python3
"""a caching system module"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    a class FIFOCache that inherits from BaseCaching
    and is a caching system with a limit
    """
    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                for k in self.cache_data.keys():
                    print(f"DISCARD: {k}")
                    del self.cache_data[k]
                    break

    def get(self, key):
        """
        Get an item by key from the cache
        """
        if key:
            return self.cache_data.get(key)
