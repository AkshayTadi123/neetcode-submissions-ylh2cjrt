class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1, map2 = {}, {}
        if len(s) != len(t):
            return False;
        for i in range(len(s)):
            map1[s[i]] = 1 + map1.get(s[i],0)
            map2[t[i]] = 1 + map2.get(t[i],0)
        for element in map1:
            if(map1[element]!= map2.get(element,0)):
                return False

        return True
        