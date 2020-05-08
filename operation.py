from LRUCache import LRUCache
from bloom_filter import BloomFilter


class operation():
    def __init__(self, client_ring):
        self.client_ring = client_ring
        self.bloomfilter = BloomFilter(300, 0.1)
        self.cache = LRUCache

    def lru_cache(self, size):
        def decorator(func):
            if self.cache.get(key)
                

                


            return decorator
