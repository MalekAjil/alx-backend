#!/usr/bin/env python3
"""lru_cache"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache (BaseCaching):
    """LRU Cache class"""
    def __init__(self):
        """iniitialization"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for
        the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
        must discard the least recently used item put in cache (FIFO algorithm)
        must print DISCARD: with the key discarded and following by a new line
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lruk = self.order.pop(0)
            del self.cache_data[lruk]
            print("DISCARD:", lruk)
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None."""
        if key is None or key not in self.cache_data:
            return None
        self.order.remove(key)
        self.order.append(key)
        return self.cache_data[key]
