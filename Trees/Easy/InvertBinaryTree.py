"""
Invert the Binary Tree.
"""
from typing import Self

class TreeNode:
    def __init__(self, val: int, left: Self | None = None, right: Self | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right

# O(n)
# O(n)
def invertTree(node: TreeNode | None) -> None:
    if node is None:
        return 
    else:
        invertTree(node.left)
        invertTree(node.right)

        temp = node.left
        node.left = node.right
        node.right = temp


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

inverted = invertTree(a)
print(a.left.left.val == 7)

b = a.left.left
inverted = invertTree(b)
print(b.val == 7)