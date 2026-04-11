class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        while(start<end):
            if(nums[start]<nums[end]):
                return nums[start]
            index = (start + end)//2
            if(nums[index]>=nums[start]):
                start = index+1
            else:
                end = index

        return nums[start]