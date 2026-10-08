class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        total_product = 1
        temp = None
        for i in range(len(nums)):
            if nums[i] == 0:
                temp = total_product
            elif temp and temp!=0:
                temp *= nums[i]
            total_product *= nums[i]
        
        for i in range(len(nums)):
            if nums[i]==0:
                result.append(temp)
            else:
                result.append(int(total_product/nums[i]))
        return result