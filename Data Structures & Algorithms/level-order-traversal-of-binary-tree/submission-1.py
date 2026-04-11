# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        q = collections.deque()
        q.append(root)

        while q:
            list1 = []
            for i in range(len(q)):
                node = q.popleft()
                if(node):
                    q.append(node.left)
                    q.append(node.right)
                    list1.append(node.val)
            if(list1):
                result.append(list1)
        return result
            
            