# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root:
            return max(
                self.maxDepth(root.left) + self.maxDepth(root.right),
                self.diameterOfBinaryTree(root.left),
                self.diameterOfBinaryTree(root.right),
            )
        return 0
