"""
Implement queue with enquee and dequeue operations.

Solution 
    - Singly Linked List 
        - enqueue - O(1) since adding at the back
        - dequeue - O(1) removing from the front
"""
from typing import Self

class Node:
    def __init__(self, val: int, next: None | Self = None, prev: None | Self = None) -> None:
        self.val = val
        self.next = next
        self.prev = prev
    

class Queue:
    def __init__(self, nums: list) -> None:
        self.front = Node(-1)
        self.back = Node(-1)

        curr = self.front
        for num in nums:
            new_node = Node(num)
            new_node.prev = curr

            curr.next = new_node

            curr = curr.next
        
        curr.next = self.back
        self.back.prev = curr

    def enqueue(self, val: int) -> None:

        new_node = Node(val)
        
        prev = self.back.prev
        curr = self.back

        prev.next = new_node
        new_node.prev = prev

        new_node.next = curr
        curr.prev = new_node

    
    def dequeue(self) -> int | None:

        if self.front.next is self.back:
            return None
        
        node = self.front.next
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

        return node.val


queue = Queue([1, 2, 3, 4, 5])
print(queue.dequeue() == 1)
print(queue.enqueue(10) is None)
print(queue.dequeue() == 2)