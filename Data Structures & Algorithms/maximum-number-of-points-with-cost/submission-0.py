class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        m, n = len(points), len(points[0])
        dp = points[0]
        for r in range(1, m):
            new_dp = [0] * n
            for c in range(n):
                best_prev = max(dp[k] - abs(k - c) for k in range(n))
                new_dp[c] = points[r][c] + best_prev
            dp = new_dp   

        return max(dp)