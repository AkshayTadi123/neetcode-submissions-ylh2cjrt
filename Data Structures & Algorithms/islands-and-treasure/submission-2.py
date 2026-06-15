class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        distance = 0

        def helper(r, c):
            if r<0 or c<0 or r>=rows or c>=cols or grid[r][c] == -1 or (r,c) in visit:
                return
            
            visit.add((r,c))
            q.append((r,c))
        
        for t_r in range(len(grid)):
            for t_c in range(len(grid[0])):
                if grid[t_r][t_c] == 0:
                    q.append((t_r, t_c))
                    visit.add((t_r, t_c))

        while q:
            for i in range(len(q)):
                (r, c) = q.popleft()
                grid[r][c] = distance
                helper(r+1, c)
                helper(r-1, c)
                helper(r, c+1)
                helper(r, c-1)
            distance+=1

        


        

    