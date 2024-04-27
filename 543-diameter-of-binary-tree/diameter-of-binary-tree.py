# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_d = 0
        self.dfs(root)
        return self.max_d
    
    def dfs(self, root: Optional[TreeNode]) -> int:
        if root:
            left = self.dfs(root.left)
            right = self.dfs(root.right)
            self.max_d = max(self.max_d, left + right)
            return max(left, right) + 1
        return 0
