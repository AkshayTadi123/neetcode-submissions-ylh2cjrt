class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        total_product = 1
        x = False
        temp = None
        for i in range(len(nums)):
            if nums[i] == 0:
                if x:
                    total_product = 0
                x = True
            else:
                total_product *= nums[i]
        
        for i in range(len(nums)):
            if not x:
                result.append(int(total_product/nums[i]))
            else:
                if nums[i]==0:
                    result.append(int(total_product))
                else:
                    result.append(0)

        return result