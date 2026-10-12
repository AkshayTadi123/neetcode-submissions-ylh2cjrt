class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
    
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]


        # fn to find the parent of a node
        def find(node):
            while parent[node] != node:
                node = parent[node]
            return node
        
        # fn to try and combine two nodes
        def union(node1, node2):

            p1, p2 = find(node1), find(node2)

            if p1 == p2:
                return 0

            if rank[p1]>rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return 1

        result = n
        for edge1, edge2 in edges:
            result -= union(edge1, edge2)

        return result