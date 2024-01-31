#!/usr/bin/python3
"""a caching system module"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    a class that inherits from BaseCaching
    and is a caching system with a LFU limit
    """
    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()
        self.key_count = {}

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:

            if len(self.cache_data) >= self.MAX_ITEMS and\
                 key not in self.cache_data:

                lfu_key = sorted(
                    self.key_count.items(),
                    key=lambda item: item[1]
                )

                print(f"DISCARD: {lfu_key[0][0]}")
                del self.cache_data[lfu_key[0][0]]
                del self.key_count[lfu_key[0][0]]

            self.cache_data[key] = item

            if key in self.key_count:
                self.key_count[key] += 1
            else:
                self.key_count[key] = 1

    def get(self, key):
        """
        Get an item by key from the cache
        """
        if key in self.cache_data.keys():
            self.key_count[key] += 1
        return self.cache_data.get(key)
