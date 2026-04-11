# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxSum = -float('inf')

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -float('inf')
        def helper(node):
            if not node:
                return 0
            
            val1 = max(helper(node.left), 0)
            val2 = max(helper(node.right), 0)
            self.maxSum = max(self.maxSum, val1+node.val+val2)
            return node.val+max(0, val1, val2)

        temp = helper(root)
        return max(self.maxSum, temp)