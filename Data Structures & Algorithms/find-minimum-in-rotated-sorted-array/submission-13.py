class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        result = float('inf')

        while(left<=right):
            index = (left+right)//2
            if(nums[left]<nums[right]):
                result = min(result, nums[left])
            
            if(nums[index]>=nums[left]):
                left = index+1
                result = min(result, nums[index])
            else:
                right = index-1
                result = min(result, nums[index])

        return result

            
            
