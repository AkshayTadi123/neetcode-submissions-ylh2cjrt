class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dict1 = {}
        subarray_sums = []
        temp = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                if((i,j) in dict1):
                    subarray_sums.append(dict1[(i,j)])
                else:
                    temp = nums[i:j]
                    subarray_sums.append(sum(temp))
                    dict1[(i,j)] = sum(temp)
                    temp = []
        subarray_sums.sort()
        return  subarray_sums[-1]
        