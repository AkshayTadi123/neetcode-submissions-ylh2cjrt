# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        unsorted = []
        self.dfs(root, unsorted)
        return unsorted[k-1]
    
    def dfs(self, root: Optional[TreeNode], array: List[TreeNode]):
        if(root):
            self.dfs(root.left, array)
            array.append(root.val)
            self.dfs(root.right, array)

        
