"""
Convert the sorted array to BST.
"""

from typing import Self

class TreeNode:
    def __init__(self, val: int, left: Self | None = None, right: Self | None = None):
        self.val = val
        self.left = left
        self.right = right

# O(nlogn)
# O(nlogn)
def convertToBST(lst: list) -> TreeNode:
    if len(lst) == 0:
        return None
    else:
        mid = len(lst) // 2
        node = TreeNode(lst[mid])

        left_subtree = convertToBST(lst[:mid])
        right_subtree = convertToBST(lst[mid+1:])

        node.left = left_subtree
        node.right = right_subtree
        
        return node


# O(n)
# O(log n)
def optimalConvertToBST(start, end):
    if start >= end:
        return None
    else:
        mid = start + (end - start) // 2
        node = TreeNode(lst[mid])

        left_subtree = optimalConvertToBST(start, mid)
        right_subtree = optimalConvertToBST(mid + 1, end)

        node.left = left_subtree
        node.right = right_subtree

        return node


lst = [1, 2, 3, 4, 5, 6]
print(convertToBST(lst))
print(optimalConvertToBST(0, len(lst)))