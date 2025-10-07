"""
Find the LCA (Lowest Common Ancestor) in Binary Tree

Example: [3, 5, 1, 6, 2, 0, 8], p = 5, q = 1 → 3
"""

from typing import Self
from collections import deque

class TreeNode:
    def __init__(self, val: int, left: Self | None = None, right: Self | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right

# O(n)
# O(n)

def findLCA(node: TreeNode, p: int, q: int) -> TreeNode | None:
    if node is None:
        return None
    
    if node.val == p or node.val == q:
        return node
    
    left = findLCA(node.left, p, q)
    right = findLCA(node.right, p, q)

    if left is not None and right is not None:
        return node
    elif left is not None:
        return left
    elif right is not None:
        return right
    else:
        return None

# 4
#   2
#       1
#       3
#   6
#       5
#       7
#

a = TreeNode(4)
a.left = TreeNode(2)
a.left.left = TreeNode(1)
a.left.right = TreeNode(3)

a.right = TreeNode(6)
a.right.left = TreeNode(5)
a.right.right = TreeNode(7)

# Test cases
print("LCA of 7 and 2:", findLCA(a, 7, 2).val)  # Should be 4
print("LCA of 1 and 3:", findLCA(a, 1, 3).val)  # Should be 2
print("LCA of 5 and 7:", findLCA(a, 5, 7).val)  # Should be 6
print("LCA of 1 and 5:", findLCA(a, 1, 5).val)  # Should be 2