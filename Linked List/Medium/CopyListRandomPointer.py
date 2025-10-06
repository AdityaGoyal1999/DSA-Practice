"""
Copy the list with next and random pointer.

Random pointer points to random nodes in the list.
"""
from typing import Self

class Node:
    def __init__(self, val: int, next: Self | None = None, random: Self | None = None) -> None:
        self.val = val 
        self.next = next
        self.random = random

def printLL(ll: Node | None) -> None:

    curr = ll
    while curr:
        random_val = "None" if curr.random is None else str(curr.random.val)
        print(f"{curr.val} -> {random_val}")
        curr = curr.next

# O(n)
# O(n)
def copyList(ll: Node | None) -> Node | None:
    nodes = {None: None}

    # create copies
    curr = ll
    while curr:
        nodes[curr] = Node(curr.val)
        curr = curr.next

    # connect random pointers of copies
    curr = ll
    while curr:
        nodes[curr].next = nodes[curr.next]
        nodes[curr].random = nodes[curr.random]

        curr = curr.next
    
    return nodes[ll]

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.next = b
b.next = c
c.next = d

a.random = c
b.random = a
c.random = d
d.random = b

printLL(a)

print("=" * 50)

new_ll = copyList(a)
printLL(new_ll)