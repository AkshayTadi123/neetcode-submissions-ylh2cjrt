class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V": 5, "X": 10, "L":50, "C":100, "D":500, "M":1000}
        result = 0
        for i in range(len(s)):
            if(i!=len(s)-1):
                if(s[i]=="I"):
                    if s[i+1]=="V" or s[i+1]=="X":
                        result -= 2
                elif(s[i]=="X"):
                    if s[i+1]=="L" or s[i+1]=="C":
                        result -= 20
                elif(s[i]=="C"):
                    if s[i+1]=="D" or s[i+1]=="M":
                        result -= 200
            
            result += roman[s[i]]
        
        return result


                
            


        