"""
Traverse a linked list
"""
from typing import Self

class Node:
    def __init__(self, val: int, next: Self | None = None):
        self.val = val
        self.next = next

# O(n)
# O(1) auxillary space used. Only space needed was for creating Linked List nodes
def getLinkedList(nums: list) -> Node:
    
    dummyHead = Node(-1)
    curr = dummyHead
    
    for num in nums:
        node = Node(num)
        curr.next = node
        curr = curr.next
    
    return dummyHead.next


# O(n)
# O(1) auxillary

def traverse(ll: Node | None) -> list:

    curr = ll
    result = []

    while curr is not None:
        result.append(curr.val)
        curr = curr.next
    
    return result

nums = [1, 2, 3, 4, 5]
ll = getLinkedList(nums)
print(traverse(ll))