# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    i = 0
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node, res):
            if node:
                res.append(str(node.val))
                dfs(node.left, res)
                dfs(node.right, res)
            else:
                res.append("N")
        dfs(root, res)
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        array = data.split(",")
        self.i = 0
        
        def dfs2(array):

            if(self.i >= len(array)):
                return None
            if(array[self.i]=="N"):
                self.i += 1
                return None
            
            node = TreeNode(int(array[self.i]))
            self.i += 1
            node.left = dfs2(array)
            node.right = dfs2(array)
            return node
        
        return dfs2(array)

            


        

            