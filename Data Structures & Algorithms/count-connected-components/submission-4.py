class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
    
        result = 0
        visit = set()
        adj_matrix = {}
        for i in range(n):
            adj_matrix[i] = []

        for i in range(len(edges)):
            [a,b] = edges[i]
            adj_matrix[a].append(b)
            adj_matrix[b].append(a)
        
        print(adj_matrix)

        def helper(node):
            if node in visit:
                return
            visit.add(node)
            for j in range(len(adj_matrix[node])):
                helper(adj_matrix[node][j])
        
        for i in range(n):
            if i in visit:
                continue
            result += 1
            helper(i)
        
        return result