class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        map = {}

        def helper(index1, index2):
            if (index1, index2) in map:
                return map[(index1, index2)]

            if index1 == len(word1):
                return len(word2) - index2
            
            if index2 == len(word2):
                return len(word1) - index1
            
            if word1[index1] == word2[index2]:
                return helper(index1+1, index2+1)

            map[(index1, index2)]  = min(
                1+ helper(index1+1, index2), #delete char 
                1+ helper(index1, index2+1), #insert char
                1+ helper(index1+1, index2+1) #replace char
            )

            return map[(index1, index2)]
        
        return helper(0, 0)