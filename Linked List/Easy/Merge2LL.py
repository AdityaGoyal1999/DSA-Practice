"""
Merge 2 sorted Linked Lists
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


# O(n + m) runtime 
# O(1) space
def mergeSortedLL(list1: Node | None, list2: Node | None) -> Node | None:

    dummyHead = Node(-1)

    curr1 = list1
    curr2 = list2
    curr = dummyHead

    while curr1 is not None and curr2 is not None:
        if curr1.val <= curr2.val:
            curr.next = curr1
            curr1 = curr1.next
        else:
            curr.next = curr2
            curr2 = curr2.next
        
        curr = curr.next
    
    if curr1 is not None:
        curr.next = curr1
    if curr2 is not None:
        curr.next = curr2
    
    return dummyHead.next


nums = [1, 2, 3]
list1 = getLinkedList(nums)

nums = [1, 2, 3]
list2 = getLinkedList(nums)

mergedList = mergeSortedLL(list1, list2)

curr = mergedList
while curr is not None:
    print(curr.val)
    curr = curr.next

