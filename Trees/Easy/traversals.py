"""
Different traversals for Trees
- Inorder
- Preorder
- Postorder
"""

from typing import Self
from collections import deque

class TreeNode:

    def __init__(self, val: int, left: Self | None = None, right: Self | None = None) -> None:
        self.val = val
        self.left = None
        self.right = None


class Traversal:

    def __init__(self, node: TreeNode) -> None:
        self.tree = node

    def inorder(self) -> list:
        # O(n) runtime
        # O(n) space

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

    def inorderIterative(self) -> list:
        # O(n) runtime - visit each node once
        # O(n) space - stack can hold up to h nodes (height of tree)
        
        result = []
        stack = []
        current = self.tree
        
        while stack or current:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process the current node
            current = stack.pop()
            result.append(current.val)
            
            # Move to right subtree
            current = current.right
        
        return result
    
    def preorder(self) -> list:
        # O(n) runtime
        # O(n) space

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
    
    def preorderIterative(self) -> list:
        # O(n) runtime - visit each node once
        # O(n) space - stack can hold up to h nodes (height of tree)
        
        result = []
        stack = []
        current = self.tree
        
        while stack or current:
            # Process current node first (Root)
            if current:
                result.append(current.val)
                
                # Push right child first, then left
                # This ensures left is processed before right
                if current.right:
                    stack.append(current.right)
                if current.left:
                    stack.append(current.left)
                
                # Move to left child (or pop from stack)
                current = current.left
            else:
                # Pop from stack when no more left children
                current = stack.pop()
        
        return result


    def postorder(self) -> list:
        # O(n) runtime
        # O(n) space

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
    
    def levelOrderTraversal(self) -> list:
        # O(n) runtime
        # O(n) space

        result = []

        def traverse(node):
            queue = deque()

            queue.append(node)
            while queue:
                length = len(queue)

                for _ in range(length):
                    node = queue.popleft()
                    result.append(node.val)

                    if node.left is not None:
                        queue.append(node.left)
                    if node.right is not None:
                        queue.append(node.right)
        
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
print("Inorder (Recursive):", traversal.inorder())
print("Inorder (Iterative):", traversal.inorderIterative())
print("Preorder (Recursive):", traversal.preorder())
print("Preorder (Iterative):", traversal.preorderIterative())
print("Postorder:", traversal.postorder())
print("Level Order Traversal:", traversal.levelOrderTraversal())