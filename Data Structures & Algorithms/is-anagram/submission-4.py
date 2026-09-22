class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = defaultdict(int)
        map2 = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in map1:
                map1[s[i]] += 1
            else:
                map1[s[i]] = 1

            if t[i] in map2:
                map2[t[i]] += 1
            else:
                map2[t[i]] = 1

        if (len(map1.keys()) != len(map2.keys())):
            return False

        for key in map1:
            if key not in map2 or map1[key]!=map2[key]:
                return False
        return True
