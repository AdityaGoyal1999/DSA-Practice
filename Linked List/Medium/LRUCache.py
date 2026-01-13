"""
Implement LRU Cache.
"""
from typing import Self

class Node:
    def __init__(self, key: int, val: int, next: Self | None = None, prev: Self | None = None) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = {} 
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val     
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.add(node)
        if len(self.cache) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]
    
    def remove(self, node: Node) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def add(self, node: Node) -> None:
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node   

# O(1) runtime 
# O(1) space
# O(1) auxillary space
# O(1) time complexity
# O(1) space complexity
# O(1) auxillary space complexity
# O(1) time complexity
# O(1) space complexity
# O(1) auxillary space complexity

# Example usage:
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  # Output: 1
lru.put(3, 3)      # Evicts key 2
print(lru.get(2))  # Output: -1 (not found)
lru.put(4, 4)      # Evicts key 1
print(lru.get(1))  # Output: -1 (not found)
print(lru.get(3))  # Output: 3
print(lru.get(4))  # Output: 4