class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        coordinates = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()
        q = deque()
        fresh = 0
        result = 0
        rotten_fruits = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rotten_fruits.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        for fruit in rotten_fruits:
            q.append((fruit, 0))

        while q:
            ((x_coord, y_coord), minutes) = q.popleft()
            result = max(result, minutes)
            for a, b in coordinates:
                if x_coord+a >=0 and x_coord+a<len(grid) and y_coord+b>=0 and y_coord+b<len(grid[0]) and grid[x_coord+a][y_coord+b]==1:
                    grid[x_coord+a][y_coord+b]=2
                    fresh -= 1
                    q.append(((x_coord+a, y_coord+b), minutes+1))
        
        return result if fresh==0 else -1
