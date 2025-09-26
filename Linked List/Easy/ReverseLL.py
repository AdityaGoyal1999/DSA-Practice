"""
Reverse a linked list.
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


# O(n) runtime 
# O(1) space

# recursive reversal of linked list
def reverseLL(ll: Node | None) -> Node | None:
    prev = None
    curr = ll

    while curr is not None:
        temp = curr.next

        curr.next = prev

        prev = curr
        curr = temp
    
    return prev

# TODO: implement recursive solution

nums = [1, 2, 3, 4]
ll = getLinkedList(nums)

new_ll = reverseLL(ll)

curr = new_ll

while curr:
    print(curr.val)
    curr = curr.next
