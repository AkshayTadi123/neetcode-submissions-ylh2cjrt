class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        people_who_trust = []
        mapp = defaultdict(list)
        for i in range(len(trust)):
            temp = trust[i][0]
            mapp[trust[i][1]].append(temp)
            if temp not in people_who_trust:
                people_who_trust.append(temp)
        
        for key, val in mapp.items():
            if len(val) == n-1 and key not in val and key not in people_who_trust:
                return key
            
        return -1

        