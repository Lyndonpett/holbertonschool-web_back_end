#!/usr/bin/env python3
"""Creating a class BasicCache that inherits from BaseCaching"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching"""

    def put(self, key, item):
        """Add an item in the cache"""
        if (key and item):
            self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if (key):
            return self.cache_data.get(key)
