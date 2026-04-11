# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = True
        minVal = -float('inf')
        maxVal = float('inf')
        return self.isValid(root, minVal, maxVal)
        

    def isValid(self, root: Optional[TreeNode], minVal: int, maxVal: int) -> bool:
        if root:
            result = root.val<maxVal and root.val>minVal
            return result and self.isValid(root.left, minVal, root.val) and self.isValid(root.right, root.val, maxVal)
        return True