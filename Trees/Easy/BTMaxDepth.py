"""
Maximum Depth of Binary Tree
"""
from typing import Self

class TreeNode:
    def __init__(self, val, left: Self | None = None, right: Self | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right

# O(n) runtime
# O(n) space
def getDepth(node):
    if node is None:
        return 0
    else:
        left_depth = getDepth(node.left)
        right_depth = getDepth(node.right)

        return 1 + max(left_depth, right_depth)

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

print(getDepth(a) == 3)