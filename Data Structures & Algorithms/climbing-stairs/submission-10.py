class Solution:

    seen = {}

    def climbStairs(self, n: int) -> int:
        if n==0:
            return 1
        if n<0:
            return 0
        
        if n in self.seen:
            return self.seen[n]

        self.seen[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.seen[n]
        