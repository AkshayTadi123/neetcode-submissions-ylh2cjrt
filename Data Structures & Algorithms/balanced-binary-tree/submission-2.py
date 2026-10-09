# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node):
            if node:
                x = helper(node.left)
                y = helper(node.right)
                z = x[0] and y[0] and abs(x[1] - y[1]) <= 1
                return [z, 1+max(x[1], y[1])]
            return [True,0]
        
        return helper(root)[0]
        

        
                    
                