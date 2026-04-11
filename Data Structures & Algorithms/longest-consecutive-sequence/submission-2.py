class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(nums == []):
            return 0
        nums.sort()
        maxCount = 0
        count = 0
        for i in range(1,len(nums)):
            if(nums[i]-nums[i-1] == 1):
                count+=1
            elif(nums[i]-nums[i-1] == 0):
                count+=0
            else:
                maxCount = max(maxCount, count)
                count = 0
        maxCount = max(maxCount, count)
        return maxCount+1




            
        