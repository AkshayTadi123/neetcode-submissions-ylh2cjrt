class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        subarray_sums = []
        temp = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                temp = nums[i:j]
                subarray_sums.append(sum(temp))
                temp = []
        subarray_sums.sort()
        return  subarray_sums[-1]
        