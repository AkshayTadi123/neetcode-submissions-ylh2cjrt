class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.dp = {}
        def helper(i, j):
            if(i,j) in self.dp:
                return self.dp[(i,j)]
            if i == m-1 and j == n-1:
                return 1
            
            if not(i in range(m) and j in range(n)):
                return 0
            
            self.dp[(i,j)] = helper(i+1, j) + helper(i, j+1)
            return self.dp[(i,j)]
        
        return helper(0,0)
                
            
