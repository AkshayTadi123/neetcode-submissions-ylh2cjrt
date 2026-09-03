class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        map = defaultdict(list)
        for i,num in enumerate(nums):
            map[num].append(i)

        for key in map.keys():
            for j in range(len(map[key])-1):
                if (map[key][j+1] - map[key][j]) <= k:
                    return True
            
        return False

