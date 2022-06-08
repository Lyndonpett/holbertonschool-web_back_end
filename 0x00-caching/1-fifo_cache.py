#!/usr/bin/env python3
"""Creating a class FIFOCache that inherits from BaseCaching"""


from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """FIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initiliaze the cache"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Puts an item in the cache in FIFO"""
        if (key and item):
            self.cache_data[key] = item
            if (len(self.cache_data) > self.MAX_ITEMS):
                key, val = self.cache_data.popitem(last=False)
                print("DISCARDED: {}".format(key))

    def get(self, key):
        """Gets an item by key"""
        if key or key in self.cache_data:
            return self.cache_data.get(key)
