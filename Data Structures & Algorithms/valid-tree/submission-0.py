class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_matrix = {i: [] for i in range(n)}
        for a, b in edges:
            adj_matrix[a].append(b)
            adj_matrix[b].append(a)
        
        visit = set()
        
        def dfs(node, parent):
            if node in visit:
                return False  # found a cycle
            visit.add(node)
            
            for nei in adj_matrix[node]:
                if nei == parent:
                    continue  # don’t revisit the parent
                if not dfs(nei, node):
                    return False
            return True
        
        # check both cycle-freeness and connectivity
        return dfs(0, -1) and len(visit) == n
        
        

        