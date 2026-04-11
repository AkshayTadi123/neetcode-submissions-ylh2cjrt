# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        maxVal = max(p.val, q.val)
        minVal = min(p.val, q.val)
        if (maxVal>=root.val and minVal<=root.val):
            return root
        elif(maxVal>root.val and minVal>root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return self.lowestCommonAncestor(root.left, p, q)


        