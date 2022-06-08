#!/usr/bin/env python3
"""Creating class LIFOCache that inherits from BaseCaching"""


from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching"""

    def __init__(self):
        """Initiliaze the cache"""
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """Add an item in the cache"""
        if (key and item):
            self.cache_data[key] = item

            if (key not in self.cache_list):
                self.cache_list.append(key)

            if (len(self.cache_data) > self.MAX_ITEMS):
                discardKey = self.cache_list.pop(self.MAX_ITEMS - 1)
                print("DISCARD: {}".format(discardKey))
                del self.cache_data[discardKey]

    def get(self, key):
        """Get an item by key"""
        if key or key not in self.cache_data:
            return self.cache_data.get(key)
