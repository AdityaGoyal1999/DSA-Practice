"""
Different traversals for Trees
- Inorder
- Preorder
- Postorder
"""

from typing import Self

class TreeNode:

    def __init__(self, val: int, left: Self | None = None, right: Self | None = None) -> None:
        self.val = val
        self.left = None
        self.right = None


class Traversal:

    def __init__(self, node: TreeNode) -> None:
        self.tree = node

    def inorder(self) -> list:
        result = []

        def traverse(node):
            if not node:
                return
            else:
                traverse(node.left)
                result.append(node.val)
                traverse(node.right)
        
        traverse(self.tree)
        return result
    
    def preorder(self) -> list:
        result = []

        def traverse(node):
            if not node:
                return
            else:
                result.append(node.val)
                traverse(node.left)
                traverse(node.right)
        
        traverse(self.tree)
        return result
    
    def postorder(self) -> list:
        result = []

        def traverse(node):
            if not node:
                return 
            else:
                traverse(node.left)
                traverse(node.right)
                result.append(node.val)
        
        traverse(self.tree)
        return result

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

traversal = Traversal(a)
print("Inorder:", traversal.inorder())
print("Preorder:", traversal.preorder())
print("Postorder:", traversal.postorder())