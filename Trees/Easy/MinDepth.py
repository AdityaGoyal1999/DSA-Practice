"""
Find the minimum depth of the tree.

Intuition:
- Shortest root to leave path.
"""
from typing import Self

class TreeNode:
    def __init__(self, val: int, left: Self | None = None, right: Self | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right

# O(n)
# O(n)
def minimumDepth(root) -> int:
    """
    This is specifically to find the distance between root and leaf node.
    """

    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1
    elif root.left is None:
        return 1 + minimumDepth(root.right)
    else:
        return 1 + minimumDepth(root.left)


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
# a.left.right = TreeNode(5)

# a.right = TreeNode(3)
# a.right.left = TreeNode(6)
# a.right.right = TreeNode(7)

print(minimumDepth(a))