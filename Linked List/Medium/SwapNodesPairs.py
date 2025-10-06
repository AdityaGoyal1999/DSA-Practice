"""
Swap the nodes in pairs.

[1,2,3,4] → [2,1,4,3]

# TODO: started with a wierd tuple (start, end) approach at the beginning. Retry this question.
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Easy'))
from SinglyLL import Node, getLinkedList, printLinkedList

# O(n)
# O(n)
def swapNodes(node: Node | None) -> Node | None:
    
    if node is None or node.next is None:
        return node

    first = node
    second = node.next

    third = second.next
    new_third = swapNodes(third)

    first.next = new_third
    second.next = first

    return second

nums = [1, 2, 3, 4, 5]
ll = getLinkedList(nums)
printLinkedList(ll)

print("=" * 50)
new_ll = swapNodes(ll)
printLinkedList(new_ll)