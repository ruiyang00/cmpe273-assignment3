from DoubleLinkedlist import DoubleLinkedlist
from LRUCache import LRUCache

map = {}
cache = []


def lru_cache(max_size):
    return None


def setItem(key, value):
    cache.append(value)
    map[key] = cache[0]


def getItem():
    return None
