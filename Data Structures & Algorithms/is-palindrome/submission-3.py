class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.lower() 
        new_str = ""
        for char in new_s:
            if(char.isalnum()):
                new_str = new_str + char

        i = 0
        j = len(new_str)-1

        while(i<=j):
            if(new_str[i]!=new_str[j]):
                return False
            i+=1
            j-=1
        return True
