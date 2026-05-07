class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        i = 2
        while n:
            if n%2 == 1:
                res += 1
            n = n//2
        return res