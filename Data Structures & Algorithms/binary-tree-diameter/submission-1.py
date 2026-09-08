# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        self.diameter = 0
        def maxDepth(root: TreeNode | None) -> int:
            if root is None: return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)
            self.diameter = max(left + right, self.diameter)
            return max(left, right) + 1
        maxDepth(root)
        return self.diameter
