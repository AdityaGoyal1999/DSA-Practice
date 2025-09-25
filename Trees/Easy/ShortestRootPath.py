"""
Shortest root to leaf path length.

[2,null,3,null,4,null,5,null,6] → 5

Could've returned 1 as 2's left subtree is None. But root cannot be leaf I suppose.
"""
from typing import Self

class TreeNode:
    def __init__(self, val: int, left: Self | None = None, right: Self | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    
def shortestPath(node):
    if node is None:
        return float("inf")
    elif node.left is None and node.right is None:
        return 1
    else:
        return 1 + min(shortestPath(node.left), shortestPath(node.right))

# 1
#   2
#       4
#       5
#   3
#       6
#       7
#

a = TreeNode(1)
# a.left = TreeNode(2)
# a.left.left = TreeNode(4)
# a.left.right = TreeNode(5)

a.right = TreeNode(3)
a.right.left = TreeNode(6)
a.right.right = TreeNode(7)

print(shortestPath(a))