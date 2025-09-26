"""
Flatten the BST to Linked List

[1,2,5,3,4,null,6] → 1→2→3→4→5→6
Preorder traversal threading
"""

from typing import Self
from collections import deque

class TreeNode:
    def __init__(self, val: int, left: Self | None = None, right: Self | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Node:
    def __init__(self, val: int, next: Self | None = None) -> None:
        self.val = val
        self.next = next

def llToList(ll: Node | None) -> Node | None:
    result = []

    curr = ll
    while curr is not None:
        result.append(curr.val)
        curr = curr.next
    
    return result

# O(n) runtime
# O(n) space
def flattenBST(root: TreeNode | None) -> Node | None:
    
    dummyNode = Node(-1)
    curr = dummyNode

    def preorderTraverse(root: TreeNode | None) -> None:
        nonlocal curr
        if root is None:
            return
        else:
            curr.next = Node(root.val)
            curr = curr.next

            preorderTraverse(root.left)
            preorderTraverse(root.right)
    
    preorderTraverse(root)
    return dummyNode.next
    

# 4
#   2
#       1
#       3
#   6
#       5
#       7
#

a = TreeNode(4)
a.left = TreeNode(2)
a.left.left = TreeNode(1)
a.left.right = TreeNode(3)

a.right = TreeNode(6)
a.right.left = TreeNode(5)
a.right.right = TreeNode(7)

ll = flattenBST(a)
print(llToList(ll))