class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for string in strs:
            map[''.join(sorted(string))].append(string)
        
        return list(map.values())