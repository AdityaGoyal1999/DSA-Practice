"""
Get Kth node's val in BST

Inorder traversal with count
"""

from typing import Self
from collections import deque

class TreeNode:
    def __init__(self, val: int, left: Self | None = None, right: Self | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def getKthNode(root: TreeNode | None, k: int) -> int:
    count = 0

    def inorderTraverse(root):
        nonlocal count
        
        if not root:
            return None
        else:
            left = inorderTraverse(root.left)
            if left is not None:
                return left
            count += 1
            if count == k:
                return root.val
            
            return inorderTraverse(root.right)
    
    result = inorderTraverse(root)
    if result:
        return result
    else:
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

print(getKthNode(a, 6))