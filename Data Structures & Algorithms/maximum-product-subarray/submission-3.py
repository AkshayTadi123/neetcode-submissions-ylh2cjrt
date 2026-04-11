class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = maxProd = minProd = nums[0]
        for i in range(1, len(nums)):
            prevMax, prevMin = maxProd, minProd
            maxProd = max(nums[i], nums[i] * prevMax, nums[i] * prevMin)
            minProd = min(nums[i], nums[i] * prevMax, nums[i] * prevMin)
            result = max(result, maxProd)
        return result
