class Solution:
    def hammingWeight(self, n: int) -> int:
        x = bin(n)[2:]
        count = 0
        print(str(x))
        for i in str(x):
            if i == "1":
                count+=1
        return count