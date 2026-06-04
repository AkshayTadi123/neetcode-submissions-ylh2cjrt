# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return True
            height1 = self.height(node.left)
            height2 = self.height(node.right)
            if abs(height1 - height2) <= 1:
                return (dfs(node.left) and dfs(node.right))
            else:
                return False
        
        return dfs(root)
        

    def height(self, root) -> int:
        if not root:
            return 0
       
        return 1 + max(self.height(root.left), self.height(root.right))