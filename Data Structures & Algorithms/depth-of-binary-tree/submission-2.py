# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            if node:
                return max(1+helper(node.right), 1+helper(node.left))
            return 0

        return helper(root)

        
        