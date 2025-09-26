"""
Delete a node from linked list
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


def deleteNode(ll: Node | None, val: int) -> Node:
    
    if ll is None:
        return None

    dummyHead = Node(-1)
    dummyHead.next = ll
    curr = dummyHead

    while curr.next is not None:
        if curr.next.val == val:
            curr.next = curr.next.next
            return dummyHead.next
        curr = curr.next
    
    return ll


nums = [1, 2, 3, 4]
ll = getLinkedList(nums)

new_ll = deleteNode(ll, 2)

curr = new_ll

while curr:
    print(curr.val)
    curr = curr.next
