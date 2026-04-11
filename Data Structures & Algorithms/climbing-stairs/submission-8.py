class Solution:
    dic = {}

    def climbStairs(self, n: int) -> int:
        
        if(n in self.dic):
            return self.dic[n]
        
        if(n<0):
            return 0
        elif(n == 0):
            return 1
        else:
            count = 0
            count += self.climbStairs(n-1)
            count += self.climbStairs(n-2)
            self.dic[n] = count
            return count



            