class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        l = 0
        r = 1
        result = 1
        map = {}
        map[s[l]] = 0
        while r<len(s):
            if s[r] in map:
                result = max(result, r-l)
                l = max(l, map[s[r]]+1)
            map[s[r]] = r
            r+=1
        
        result = max(result, r-l)

        return result

            
            
