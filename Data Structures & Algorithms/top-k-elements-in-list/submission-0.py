class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
        s = {}
        result = []
        for i in range(len(nums)):
            s[nums[i]] = s.get(nums[i], 0) + 1
        sorted_list= sorted(s.items(), key=lambda item: item[1], reverse=True)
        for j in range(k):
            result.append(sorted_list[j][0])
        return result


   

        