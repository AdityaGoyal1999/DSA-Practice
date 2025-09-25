"""
Find the LCA (Lowest Common Ancestor) in BST

Example: [4, 2, 6, 1, 3, 5, 7], p=2, q=6 → 4
"""

from typing import Self
from collections import deque

class TreeNode:
    def __init__(self, val: int, left: Self | None = None, right: Self | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def exists(node: TreeNode, val: int) -> bool:
    if node is None:
        return False
    else:
        if node.val == val:
            return True
        if val < node.val:
            return exists(node.left, val)
        else:
            return exists(node.right, val)

# O(log n)
# O(log n)
def findLCA(node: TreeNode, p: int, q: int) -> int:
    # check if nodes exist
    p_exists = exists(node, p)
    q_exists = exists(node, q)

    if not (p_exists and q_exists):
        return -1

    # if nodes exist, find LCA 
    curr = node
    while curr is not None:
        if p == curr.val or q == curr.val:
            return curr.val
        if p <= curr.val <= q or q <= curr.val <= p:
            return curr.val
        
        if p < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    
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

print(findLCA(a, 7, 5))