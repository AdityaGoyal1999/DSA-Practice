"""
Find the LCA (Lowest Common Ancestor) in BST

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
def findLCA(node: TreeNode, p: int, q: int) -> int:
    if node is None:
        return -1
    
    if node.val == p or node.val == q:
        return node.val

    left = findLCA(node.left, p, q)
    right = findLCA(node.right, p, q)

    if left != -1 and right != -1:
        return node.val
    
    if left != -1:
        return left
    if right != -1:
        return right
    
    return -1

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

print(findLCA(a, 7, 2))