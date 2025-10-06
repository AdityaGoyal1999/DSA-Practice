"""
Rotate the linked list by k steps.

Example: [1,2,3,4,5], k=2 → [4,5,1,2,3]

Solution 
- Chop the list and put the later half in the front.
- Put the front half at the back of the list.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Easy'))
from SinglyLL import Node, getLinkedList, printLinkedList


def getLength(ll: Node | None) -> int:
    curr = ll
    length = 0

    while curr is not None:
        length += 1
        curr = curr.next
    
    return length

# O(n)
# O(1)
def rotateList(ll: Node | None, k: int) -> Node | None:

    length = getLength(ll)
    if k == 0: # nothing to rotate
        return ll

    if length % k == 0: # nothing to rotate
        return ll

    # normalization
    k = k


    i = 0
    curr = ll
    while curr is not None and i < k:
        curr = curr.next
        i += 1
    
    # k == len(list)
    if curr.next is None:
        return ll
    
    new_front = curr.next
    curr.next = None

    curr = new_front
    while curr.next is not None:
        curr = curr.next
    
    curr.next = ll

    return new_front



nums = [1, 2, 3, 4, 5]
ll = getLinkedList(nums)
printLinkedList(ll)

print("=" * 50)

k = 2
new_ll = rotateList(ll, k)
printLinkedList(new_ll)