"""
Remove nth node from the end.

 Example: [1,2,3,4,5], n=2 → [1,2,3,5]
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Easy'))
from SinglyLL import Node, getLinkedList, printLinkedList

# O(n)
# O(1)
def removeNthNode(ll: Node, n: int) -> Node | None:
    dummyNode = Node(-1)
    dummyNode.next = ll

    slow, fast = dummyNode, dummyNode
    for _ in range(n):
        fast = fast.next
    
    while fast.next is not None:
        slow = slow.next
        fast = fast.next
    
    slow.next = slow.next.next
    return dummyNode.next


nums = [1, 2, 3, 4, 5]
ll = getLinkedList(nums)
n = 2

new_ll = removeNthNode(ll, n)
printLinkedList(new_ll)