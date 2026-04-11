class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        l = 0
        charset = set()

        for r in range(len(s)):
            if s[r] in charset:
                while s[r] in charset:
                    charset.remove(s[l])
                    l += 1
            maxCount = max(maxCount, r - l +1)
            charset.add(s[r])
        
        return maxCount


        