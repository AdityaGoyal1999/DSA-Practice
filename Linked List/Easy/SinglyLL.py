"""
Implement singly linked list.
"""
from typing import Self

class Node:
    def __init__(self, val: int, next: Self | None = None):
        self.val = val
        self.next = next

# O(n)
# O(1) auxillary space used. Only space needed was for creating Linked List nodes
def getLinkedList(nums):
    
    dummyHead = Node(-1)
    curr = dummyHead
    
    for num in nums:
        node = Node(num)
        curr.next = node
        curr = curr.next
    
    return dummyHead.next


nums = [1, 2, 3, 4, 5, 6]
print(getLinkedList(nums))