# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(res: List[int], node: Optional[TreeNode]) -> None:
            if node:
                res.append(node.val)
                dfs(res, node.left)
                dfs(res, node.right)
        dfs(res, root)
        return res
