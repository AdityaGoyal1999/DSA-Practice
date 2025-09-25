"""
Create a zigzag order traversal

 [3,9,20,null,null,15,7] → [[3],[20,9],[15,7]]
"""
from typing import Self
from collections import deque

class TreeNode:
    def __init__(self, val: int, left: Self | None = None, right: Self | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right

def zigzagTraversal(node: TreeNode) -> list:
    if node is None:
        return []
    
    result = []
    def traverse(node: TreeNode) -> None:
        queue = deque()
        queue.append(node)
        level = 0

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
            
            if level % 2 == 0:
                result.append(sub_result)
            else:
                result.append(sub_result[::-1])
            
            level += 1
    
    traverse(node)
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

print(zigzagTraversal(a))