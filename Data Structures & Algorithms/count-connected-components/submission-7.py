class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parent = [i for i in range(n)]
        rank = [0]*n
        result = 0

        # finding the parent
        def find(node):
            x = node
            while parent[x] != x:
                x = parent[x]
            return x
        
        # add two components together
        def union(node1, node2):

            p1, p2 = find(node1), find(node2)
            if p1 == p2:
                return False
            
            if rank[p1]>rank[p2]:
                rank[p1] += rank[p2]
                parent[p2] = p1
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            
            return True

        for x, y in edges:
            if union(x,y):
                result += 1
            
        return n-result




            