"""
Calculate the height of the tree.
"""
from typing import Self

class TreeNode:
    def __init__(self, val, left: Self | None = None, right: Self | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right

def getTreeHeight(node):
    
    if not node:
        return 0
    else:
        # left subtree
        left_height = getTreeHeight(node.left)

        # right subtree
        right_height = getTreeHeight(node.right)

        return 1 + max(left_height, right_height)
    

# 1
#   2
#       4
#       5
#   3
#       6
#       7
#

a = TreeNode(1)
a.left = TreeNode(2)
a.left.left = TreeNode(4)
a.left.right = TreeNode(5)

a.right = TreeNode(3)
a.right.left = TreeNode(6)
a.right.right = TreeNode(7)

print(getTreeHeight(a) == 3)
print(getTreeHeight(a.right.right) == 1)
print(getTreeHeight(a.left.left.left) == 0)
