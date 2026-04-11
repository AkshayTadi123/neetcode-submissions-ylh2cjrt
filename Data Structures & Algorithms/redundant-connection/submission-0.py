class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        connections = {i: [] for i in range(1, len(edges) + 1)}

        def dfs(src, target, visited):
            if src == target:
                return True
            visited.add(src)
            for nei in connections[src]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True
            return False

        for edge1, edge2 in edges:
            # If edge1 and edge2 are already connected, this edge is redundant
            if dfs(edge1, edge2, set()):
                return [edge1, edge2]
            connections[edge1].append(edge2)
            connections[edge2].append(edge1)

            