class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        
        result = [0, 1, 1]
        for i in range(2, n):
            result.append(result[i-2]+result[i-1]+result[i])
        
        return result[-1]
