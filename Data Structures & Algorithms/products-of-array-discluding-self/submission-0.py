class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        result = []

        index = float('inf')
        for num in nums:
            if(num == 0 and index == float('inf')):
                index = nums.index(num)
            else:
                product *= num
        
        for i in range(len(nums)):
            if(index != float('inf') and i!=index):
                result.append(0)
            elif(index != float('inf') and i==index):
                result.append(product)
            else:
                result.append(product//nums[i])
            
                
        return result

        