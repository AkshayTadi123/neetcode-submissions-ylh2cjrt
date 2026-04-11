# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        self.helper1(root, result, 0)
        return result

    def helper1(self, root: Optional[TreeNode], result: Optional[TreeNode], level: int):
        if(root):
            if(level>len(result)-1):
                result.append([])
            result[level].append(root.val)
            self.helper1(root.left, result, level+1)
            self.helper1(root.right, result, level+1)