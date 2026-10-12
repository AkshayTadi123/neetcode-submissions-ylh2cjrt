class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def helper(index1, index2):
            if(index1, index2) in memo:
                return memo[(index1, index2)]
            if index1 == len(word1) and index2 == len(word2):
                return 0
            
            if index1 == len(word1):
                return len(word2) - index2

            if index2 == len(word2):
                return len(word1) - index1
            
            if word1[index1] == word2[index2]:
                return helper(index1+1, index2+1)

            memo[(index1, index2)] = 1+ min(helper(index1+1, index2), helper(index1+1, index2+1), helper(index1, index2 + 1))

            return memo[(index1, index2)]

        return helper(0,0)

