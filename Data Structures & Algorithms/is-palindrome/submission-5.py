class Solution:
    def isPalindrome(self, s: str) -> bool:
       length = len(s)-1
       index = 0
       s = s.lower()
      

       while(length>index):
            a = s[length]
            b = s[index]
            if(not a.isalnum()):
                length-=1
            elif(not b.isalnum()):
                index+=1
            else:
                index += 1
                length -= 1
                if(a!=b):
                    return False
        
       return True
        
        



