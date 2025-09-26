"""
Detect a cycle in Linked List
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
def detectCycle(ll: Node | None) -> Node | None:
    if ll is None:
        return False
    
    slow, fast = ll, ll
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        
        if fast and fast.val == slow.val:
            return True
    
    return False


# 1 -> 2 -> 3 -> 4
#           |    | 
#           6 <- 5 


nums = [1, 2, 3, 4, 5, 6, 4]
ll = getLinkedList(nums)
print(detectCycle(ll))

nums = [1, 2, 3, 4]
ll = getLinkedList(nums)
print(detectCycle(ll))

