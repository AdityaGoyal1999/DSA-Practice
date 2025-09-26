"""
Insert value at the back of the linked list
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
def insertAtBack(ll: Node | None, val: int) -> Node:
    
    node = Node(val)
    if ll is None:
        return node
    else:
        curr = ll
        while curr.next is not None:
            curr = curr.next
        
        curr.next = node

        return ll


nums = [1, 2, 3, 4]
ll = getLinkedList(nums)

new_ll = insertAtBack(ll, -1)

curr = new_ll

while curr:
    print(curr.val)
    curr = curr.next
