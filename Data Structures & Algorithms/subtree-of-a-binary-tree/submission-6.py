# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(node, sub):
            
            def helper2(node2, sub2):
                if not node2 and not sub2:
                    return True
                
                if not node2 or not sub2:
                    return False
                
                if node2.val == sub2.val:
                    return helper2(node2.right, sub2.right) and helper2(node2.left, sub2.left)
                else:
                    return False
            
            if not node:
                return False

            if sub.val == node.val:
                if helper2(node, sub):
                    return True
            
            return helper(node.left, subRoot) or helper(node.right, subRoot)
        
    
        return helper(root, subRoot)
