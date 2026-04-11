class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        maximum = 1
        for i in range(len(s)):
            #Odd length palindrome:#
            l = i - 1
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            count = r-l-1

            if count > maximum:
                maximum = count
                result = s[l+1:r] 

            #Even length Palindrome:#
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            count = r - l - 1
            if count > maximum:
                maximum = count
                result = s[l + 1:r]

        return result

                    


        