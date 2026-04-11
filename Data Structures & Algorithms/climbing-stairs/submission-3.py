class Solution:
    def climbStairs(self, n: int) -> int:
        result = 0
        if(n == 0):
            return 1
        elif(n<0):
            return 0
        else:
            result += self.climbStairs(n-1)
            result += self.climbStairs(n-2)
            return result
            



        # result = 0
        # if n>0:
        #     result += 1 + self.climbStairs(n-1)
        # if n>1:
        #     result += 1  + self.climbStairs(n-2)
        # return result