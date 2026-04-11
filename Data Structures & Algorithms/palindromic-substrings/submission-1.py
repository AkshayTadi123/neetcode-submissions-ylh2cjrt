class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += 1
            left = i-1
            right = i+1
            while left>=0 and right < len(s):
                if(s[left] == s[right]):
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break

            left = i
            right = i+1
            while left>=0 and right < len(s):
                if(s[left] == s[right]):
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break

        return count
        