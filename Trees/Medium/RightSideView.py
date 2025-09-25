"""
Right side view of the Tree

 [3,9,20,null,null,15,7] → [3, 20, 7]
"""
from typing import Self
from collections import deque

class TreeNode:
    def __init__(self, val: int, left: Self | None = None, right: Self | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right

def rightSideView(node) -> list:
    result = []

    def bfs(node):
        queue = deque()
        queue.append(node)

        while queue:
            length = len(queue)

            for i in range(length):
                _node = queue.popleft()
                if i == length - 1:
                    result.append(_node.val)
                
                if _node.left is not None:
                    queue.append(_node.left)
                if _node.right is not None:
                    queue.append(_node.right)
            
    if node is None:
        return []
    bfs(node)
    return result

# 3
#   9
#   20
#       15
#       7
#

a = TreeNode(3)
a.left = TreeNode(9)
# a.left.left = TreeNode(4)
# a.left.right = TreeNode(5)

a.right = TreeNode(20)
a.right.left = TreeNode(15)
a.right.right = TreeNode(7)

print(rightSideView(a))