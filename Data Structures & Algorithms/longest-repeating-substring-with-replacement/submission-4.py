class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        l = 0
        result = 0
        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r], 0) + 1
            max_freq = max(dic.values())
            windowLength = r - l + 1
            if(windowLength-max_freq<=k):
                result = max(result, windowLength)
            else:
                dic[s[l]] = dic.get(s[l], 0) - 1
                l += 1
        return result

