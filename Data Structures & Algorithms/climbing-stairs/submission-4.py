class Solution:
    memo = {}

    def climbStairs(self, n: int) -> int:
        if(n in self.memo):
            return self.memo[n]
        if(n == 0):
            return 1
        elif(n<0):
            return 0
        else:
            result = 0
            result += self.climbStairs(n-1)
            result += self.climbStairs(n-2)
            self.memo[n] = result
            return result
            