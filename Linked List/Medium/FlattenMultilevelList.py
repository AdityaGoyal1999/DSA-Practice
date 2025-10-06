"""
Flatten the linked list.

 Example: 1→2→(3→4) → 1→2→3→4

Solution -
    
"""
from typing import Self

class Node:
    def __init__(self, val: int, next: Self | None = None, child: Self | None = None) -> None:
        self.val = val
        self.next = next
        self.child = child

# The nodes can form a complete grid instead of just being 2 dimensional.