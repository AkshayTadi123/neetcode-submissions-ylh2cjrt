"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        def dfs(x):
            if not x:
                return None
            if x.val in mapp:
                return mapp[x.val]
            else:
                y = Node(x.val)
                mapp[x.val] = y
            
            for nei in x.neighbors:
                y.neighbors.append(dfs(nei))

            return y


        mapp = {}
        return dfs(node)