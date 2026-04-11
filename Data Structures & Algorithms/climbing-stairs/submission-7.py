class Solution:

    def climbStairs(self, n: int) -> int:
        dic = {}
        if(n in dic):
            return dic[n]
        
        if(n<0):
            return 0
        elif(n == 0):
            return 1
        else:
            count = 0
            count += self.climbStairs(n-1)
            count += self.climbStairs(n-2)
            dic[n] = count
            return count



            