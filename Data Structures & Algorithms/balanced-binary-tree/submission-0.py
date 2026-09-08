# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    @classmethod
    def isBalanced(self, root: TreeNode | None) -> bool:
        self.balanced = True
        def dfs(root: TreeNode | None) -> int:
            if root is None: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.balanced = (abs(left - right) <= 1) and self.balanced
            return max(left, right) + 1
        dfs(root)
        return self.balanced

        