"""
Get the nth node from the back
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
def getNthNode(ll: Node | None, n: int) -> Node | None:
    if ll is None:
        return None
    
    fast = ll
    slow = ll
    for _ in range(n):
        fast = fast.next
    
    while fast is not None:
        fast = fast.next
        slow = slow.next
    
    return slow

nums = [1, 2, 3, 4]
ll = getLinkedList(nums)

print(getNthNode(ll, 2).val)
print(getNthNode(ll, 3).val)
print(getNthNode(ll, 4).val)