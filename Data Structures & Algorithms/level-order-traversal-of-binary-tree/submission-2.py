# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        levels = {}

        def dfs(root, index):
            if (root):
                if index not in levels:
                    levels[index] = []
               
                levels[index].append(root.val)
                dfs(root.left, index+1)
                dfs(root.right, index+1)
        
        dfs(root, 0)
        for index, key in levels.items():
            result.append(key)
        
        return result

