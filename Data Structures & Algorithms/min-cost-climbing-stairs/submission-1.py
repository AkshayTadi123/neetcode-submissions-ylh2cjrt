class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        result = cost + [0, 0]
        for i in range(len(cost)-1, -1, -1):
            result[i] = min(cost[i] + result[i+1], cost[i] + result[i+2])
        return min(result[0], result[1])
            


