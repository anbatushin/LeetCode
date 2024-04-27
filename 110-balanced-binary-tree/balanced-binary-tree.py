# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def length(self, root: Optional[TreeNode]) -> int:
        return max(self.length(root.left), self.length(root.right)) + 1 if root else 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return (
            self.isBalanced(root.left)
            and self.isBalanced(root.right)
            and abs(self.length(root.left) - self.length(root.right)) <= 1
            if root
            else True
        )
