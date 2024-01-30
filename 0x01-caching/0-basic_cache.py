#!/usr/bin/python3
"""a caching system module"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    a class BasicCache that inherits from BaseCaching and is a caching system
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

    def get(self, key):
        """
        Get an item by key from the cache
        """
        if key:
            return self.cache_data.get(key)
