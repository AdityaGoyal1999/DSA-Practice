"""
Find the middle of the linked list
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
def getListMiddle(ll: Node | None) -> Node | None:
    if not ll:
        return None
    
    slow, fast = ll, ll

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
    
    return slow


nums = [1, 2, 3, 4, 5]
ll = getLinkedList(nums)

print(getListMiddle(ll).val)

