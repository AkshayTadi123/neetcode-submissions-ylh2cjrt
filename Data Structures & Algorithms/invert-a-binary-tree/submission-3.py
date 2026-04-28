# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root

        if curr:
            left = curr.left
            right = curr.right

            curr.left = right
            self.invertTree(curr.left)

            curr.right = left
            self.invertTree(curr.right)
        
        return root