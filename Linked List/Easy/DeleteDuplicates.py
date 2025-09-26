"""
Delete sorted duplicates

[1,1,2,3,3] → [1,2,3]
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
def deleteDuplicates(ll: Node | None) -> Node | None:
    if ll is None:
        return None
    
    dummyHead = Node(float("inf"))
    curr = dummyHead
    curr1 = ll

    while curr1 is not None:
        if curr.val != curr1.val:
            curr.next = curr1
            curr1 = curr1.next
            curr = curr.next
            curr.next = None
        else:
            curr1 = curr1.next
    
    return dummyHead.next


nums = [1, 2, 2, 3, 3, 3]
list1 = getLinkedList(nums)

mergedList = deleteDuplicates(list1)

curr = mergedList
while curr is not None:
    print(curr.val)
    curr = curr.next

