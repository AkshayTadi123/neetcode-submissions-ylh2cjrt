class Solution:
    def tribonacci(self, n: int) -> int:   
        result = [0, 1, 1]
        
        if n<=2:
            return result[n]
        
        for i in range(2, n):
            result.append(result[i-2]+result[i-1]+result[i])
        
        return result[-1]
