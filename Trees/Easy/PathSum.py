"""
Check if the given sum exists in the tree. 
The path should start from the root node and go on till a leaf
"""
from typing import Self

class TreeNode:
    def __init__(self, val, left: Self | None = None, right: Self | None = None) -> None:
        self.val = val
        self.left = left
        self.right = right


# O(n)
# O(n)
def pathSum(node, target) -> bool:
    # traverse and keep reducing the target
    if not node:
        if target == 0:
            return True
        else:
            return False
    else:
        return pathSum(node.left, target - node.val) or pathSum(node.right, target - node.val)
    

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


print(pathSum(a, 7) == True)
print(pathSum(a.left.left, 10) == False)