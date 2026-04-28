class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        l = 0
        map = {}
        for r in range(len(s)):
            if s[r] in map:
                l = max(l, map[s[r]]+1)
            
            map[s[r]] = r
            result = max(result,r-l+1)

        return result

            
            
