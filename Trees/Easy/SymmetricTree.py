"""
Check if the tree is the mirror image of itself.
"""

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
def isTreeSymmetric(node):

    def equalTree(p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        else:
            if p.val != q.val:
                return False
            if not equalTree(p.left, q.right) or not equalTree(p.right, q.left):
                return False
            
            return True
    if not node:
        return True
    return equalTree(node.left, node.right)
    

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

# 1
#   2
#       3
#       4
#   2
#       4
#       3
#

b = TreeNode(1)
b.left = TreeNode(2)
b.right = TreeNode(2)

b.left.left = TreeNode(3)
b.left.right = TreeNode(4)

b.right.left = TreeNode(4)
b.right.right = TreeNode(3)


print(isTreeSymmetric(a) == False)
print(isTreeSymmetric(b) == True)