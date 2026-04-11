# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -math.inf  # handle all-negative trees

        def helper(node):
            if not node:
                return 0

            # Compute max gain from left and right (ignore negative paths)
            left_gain = max(helper(node.left), 0)
            right_gain = max(helper(node.right), 0)

            # Path sum through this node (could be the best)
            current_sum = node.val + left_gain + right_gain
            self.maxSum = max(self.maxSum, current_sum)

            # Return best path *starting* from this node
            return node.val + max(left_gain, right_gain)

        helper(root)
        return self.maxSum