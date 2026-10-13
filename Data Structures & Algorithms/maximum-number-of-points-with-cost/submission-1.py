class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        m, n = len(points), len(points[0])
        dp = points[0]
        for r in range(1, m):
            new_dp = [0] * n
            for c in range(n):
                x = float('-inf')
                for k in range(n):
                    x = max(x, dp[k] - abs(k-c))
                new_dp[c] = x+points[r][c]
            dp = new_dp   

        return max(dp)