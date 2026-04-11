class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.lower() 
        new_str = ""
        for char in new_s:
            if(char.isalnum()):
                new_str = new_str + char
        return new_str == new_str[::-1]
