class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows,cols = len(grid), len(grid[0])
        visited = set()
        result = 0

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            visited.add((row,col))

            while q:
                r, c = q.popleft()
                directions = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
                for row1, col1 in directions:
                    if(row1 in range((rows)) and col1 in range(cols) and (row1, col1) not in visited and grid[row1][col1] == "1"):
                        q.append((row1, col1))
                        visited.add((row1, col1))
                    


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    if (r,c) not in visited:
                        bfs(r, c)
                        result += 1
        
        return result


        
        