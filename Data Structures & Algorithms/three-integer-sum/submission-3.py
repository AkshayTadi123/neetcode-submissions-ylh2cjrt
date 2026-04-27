class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l<r:
                if nums[l] + nums[r] < -(nums[i]):
                    l += 1
                elif (nums[l] + nums[r] > -(nums[i])):
                    r -= 1
                else:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
        return [list(i) for i in result]



