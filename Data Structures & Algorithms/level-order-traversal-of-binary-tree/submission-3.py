# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        level = 0
        res = []
        q = deque()
        if root:
            q.append((root, level))
        while q:
            x, y = q.popleft()
            if y == len(res):
                res.append([])

            res[y].append(x.val)
            
            if x.left:
                q.append((x.left, y+1))
            if x.right:
                q.append((x.right, y+1))
            level += 1

        return res
