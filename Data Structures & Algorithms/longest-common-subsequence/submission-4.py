class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def helper(index1, index2):
            if (index1, index2) in memo:
                return memo[(index1, index2)]

            if index1 == len(text1) or index2 == len(text2):
                return 0
            
            if text1[index1] == text2[index2]:
                return 1+ helper(index1+1, index2+1)
            
            memo[(index1, index2)] = max(helper(index1+1, index2), 
            helper(index1+1,index2+1), helper(index1, index2+1))

            return memo[(index1, index2)]
        return helper(0,0)

