"""
Check if the linked list is a palindromes

1 -> 2 -> 2 -> 1
Split list and reverse the second half. 
Then compare both lists.
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

def getLL(ll: Node | None) -> list:
    curr = ll
    result = []
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


def reverseAndSplit(ll: Node | None) -> Node | None:
    # reverse later of list
    fast = ll
    slow = ll

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next


    curr = slow
    prev = None

    while curr is not None:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev

# O(n) runtime 
# O(1) space
def isPalindrome(ll: Node | None) -> bool:
    if ll is None:
        return True
    
    first = ll
    second = reverseAndSplit(ll)

    curr1, curr2 = first, second
    while curr1 and curr2:
        if curr1.val != curr2.val:
            return False
        curr1 = curr1.next
        curr2 = curr2.next
    
    return True


nums = [1]
list1 = getLinkedList(nums)
print(isPalindrome(list1))

nums = [1, 2, 2, 1]
list1 = getLinkedList(nums)
print(isPalindrome(list1))

nums = [1, 2, 3, 2, 1]
list1 = getLinkedList(nums)
print(isPalindrome(list1))
