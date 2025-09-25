"""
Implement a doubly linked list
"""
from typing import Self

class Node:
    def __init__(self, val: int, next: Self | None = None, prev: Self | None = None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


def getDoublyLL(nums) -> Node:
    if len(nums) == 0:
        return None
    
    dummyHead = Node(-1)
    prev = dummyHead
    curr = None

    for num in nums:
        curr = Node(num)
        prev.next = curr
        curr.prev = prev
        prev = curr
    return dummyHead.next

nums = [1, 2, 3, 4, 5, 6]

ll = getDoublyLL(nums)
curr = ll

while curr:
    print(curr.val)
    curr = curr.next