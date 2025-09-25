"""
Level Order Traversal but for the bottom of the tree.

[3,9,20,null,null,15,7] → [[15,7],[9,20],[3]]
"""

from typing import Self
from collections import deque

class TreeNode:
    def __init__(self, val: int, left: Self | None = None, right: Self | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right

# O(n) runtime
# O(n) space 
def levelOrderBottom(node: TreeNode | None) -> list:
    result = []

    def traverse(node):
        queue = deque()
        queue.append(node)

        while queue:

            length = len(queue)
            sub_result = []
            for _ in range(length):
                _node = queue.popleft()
                sub_result.append(_node.val)

                if _node.left is not None:
                    queue.append(_node.left)
                if _node.right is not None:
                    queue.append(_node.right)
            result.append(sub_result)
        
    traverse(node)
    return result[::-1]


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

print(levelOrderBottom(a))