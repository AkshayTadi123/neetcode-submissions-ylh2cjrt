class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        mapp = {}
        def helper(sum1, sum2, index):
            if (sum1, sum2, index) in mapp:
                return mapp[(sum1, sum2, index)]

            if index == len(nums):
                return sum1 == sum2
            
            mapp[(sum1, sum2, index)] = helper(sum1 + nums[index], sum2, index+1) or helper(sum1, sum2 + nums[index], index+1)

            return mapp[(sum1, sum2, index)]
        
        return helper(0, 0, 0)
