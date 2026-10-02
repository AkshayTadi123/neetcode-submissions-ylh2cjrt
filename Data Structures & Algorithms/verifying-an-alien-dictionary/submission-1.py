class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapp = {}
        for i, char in enumerate(order):
            mapp[char] = i
        
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            
            j = 0
            while j< min(len(word1), len(word2)):
                char1, char2 = word1[j], word2[j]
                if mapp[char1]<mapp[char2]:
                    break
                if mapp[char1]>mapp[char2]:
                    return False
                j += 1
            
            if j == min(len(word1), len(word2)) and word1[:j] == word2[:j] and len(word1)>len(word2):
                return False

        return True
            

        
        