# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        parent = None
        curr = root
        to_insert = TreeNode(val)

        if not curr:
            return to_insert
            
        while curr:
            parent = curr
            if curr.val > val:
                curr = curr.left
            else:
                curr = curr.right

        if val>parent.val:
            parent.right = to_insert
        else:
            parent.left = to_insert
        
        return root
        


