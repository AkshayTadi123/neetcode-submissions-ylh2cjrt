class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l = 0
        result = ""
        x = min(len(word1), len(word2))
        for i in range(x):
            result += word1[i]
            result += word2[i]

        if len(word1)>x:
            result += word1[x:]
        else:
            result += word2[x:]
        
        return result



