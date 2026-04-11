class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        map1 = {}
        map2 = {}

        for i in range(26):
            map1[chr(i + 97)] = 0
            map2[chr(i + 97)] = 0

        for i in range(len(s1)):
            map1[s1[i]] += 1
            map2[s2[i]] += 1

        matches = 0
        for i in range(26):
            if(map1[chr(i + 97)]==map2[chr(i + 97)]):
                matches += 1
        l = 0
        for r in range(len(s1), len(s2)):
            if(matches == 26):
                return True

            map2[s2[r]] += 1
            if(map2[s2[r]] == map1[s2[r]]):
                matches += 1
            elif(map2[s2[r]] == 1+map1[s2[r]]):
                matches -= 1
            
            
            if(map2[s2[l]] == map1[s2[l]]):
                matches -= 1
            elif(map2[s2[l]] == map1[s2[l]]+1):
                matches += 1
            map2[s2[l]] -= 1
            l += 1
        return matches == 26
        
