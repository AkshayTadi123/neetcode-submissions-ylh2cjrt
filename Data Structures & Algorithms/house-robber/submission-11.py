class Solution:
    def rob(self, nums: List[int]) -> int:
        max_rob = [0] * (len(nums))
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0], nums[1])

        max_rob[0] = nums[0]
        max_rob[1] = max(nums[0], nums[1])

        for i in range(2,len(nums)):
            max_rob[i] = max(max_rob[i-1], max_rob[i-2]+nums[i])
        
        return max_rob[-1]
        

