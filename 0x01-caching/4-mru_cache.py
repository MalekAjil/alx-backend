#!/usr/bin/env python3
"""MRU_cache"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache (BaseCaching):
    """MRU Cache class"""
    def __init__(self):
        """iniitialization of class"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for
        the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
        must discard the most recent item put in cache (MRU algorithm)
        must print DISCARD: with the key discarded and following by a new line
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD:", self.cache_data.first().key)
                self.cache_data.pop(first())

    def get(self, key):
        """ return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None."""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
