class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        result = [False] * (len(s)+1)
        result[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if(i+len(word)<=len(s) and s[i:i+len(word)] == word):
                    result[i] = result[i+len(word)]
                    
                if(result[i]):
                    break
            
        
        return result[0]

       
            
        
