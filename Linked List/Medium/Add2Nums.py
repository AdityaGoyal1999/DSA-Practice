"""
Add two numbers which are represented as linked lists.
They are represented backwards.

 [2→4→3] + [5→6→4] = [7→0→8]
 [9->9->9] + [2] = [1->0->0->1]
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Easy'))
from SinglyLL import Node, getLinkedList, printLinkedList

# O(n + m)
# O(1) auxillary space. The only space created is to return the result.
def add2Nums(list1: Node | None, list2: Node | None) -> Node | None:
    
    curr1, curr2 = list1, list2
    dummyNode = Node(-1)
    curr = dummyNode
    carry = 0
    while curr1 is not None or curr2 is not None or carry == 1:
        if curr1 is None:
            first = 0
        else:
            first = curr1.val
            curr1 = curr1.next

        if curr2 is None:
            second = 0
        else:
            second = curr2.val
            curr2 = curr2.next
        
        digit = first + second + carry
        if digit > 9:
            carry = 1
            digit = digit % 10
        else:
            carry = 0
        
        curr.next = Node(digit)
        curr = curr.next
    
    return dummyNode.next


list1 = getLinkedList([9, 9, 9])
list2 = getLinkedList([2])

printLinkedList(list1)
print("=" * 50)
printLinkedList(list2)
print("=" * 50)
next_num = add2Nums(list1, list2)
printLinkedList(next_num)