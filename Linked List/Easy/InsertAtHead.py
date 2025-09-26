"""
Insert value at the front of the linked list
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


# O(1) runtime 
# O(1) space
def insertAtFront(ll: Node | None, val: int) -> Node:
    dummyHead = Node(-1)

    dummyHead.next = ll

    node = Node(val)

    tempNode = dummyHead.next
    dummyHead.next = node

    node.next = tempNode

    return dummyHead.next


nums = [1, 2, 3, 4]
ll = getLinkedList(nums)

new_ll = insertAtFront(ll, -1)

curr = new_ll

while curr:
    print(curr.val)
    curr = curr.next
