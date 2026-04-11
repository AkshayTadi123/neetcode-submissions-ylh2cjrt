# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums)-1
#         reqIndex = -1
#         minval = float('inf')

#         if(nums[left] <= nums[right]):
#                 return self.binary(nums, target)

#         while(left<=right):
#             index = (left+right)//2

#             if(nums[left]<=nums[index]):
#                 left = index+1
#                 reqIndex = index if nums[index] < minval else reqIndex
#                 minval = nums[index] if nums[index] < minval else minval
#             else:
#                 right = index
#                 reqIndex = index if nums[index] < minval else reqIndex
#                 minval = nums[index] if nums[index] < minval else minval
            
#         res = self.binary(nums[reqIndex:], target)
#         res2 = self.binary(nums[0:reqIndex], target)
#         if(res != -1):
#             return res + reqIndex
#         elif(res2 != -1):
#             return res2
#         else:
#             return -1
       

#     def binary(self, nums: List[int], target: int) -> int:
#         left = 0
#         right = len(nums) - 1

#         while(left<= right):
#             index = (left + right)//2

#             if(nums[index] < target):
#                 left = index+1
#             elif(nums[index] > target):
#                 right = index-1
#             else:
#                 return index

#         return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        # Step 1: Find pivot
        pivot = self.find_pivot(nums)

        # Step 2: Search in the correct half
        if nums[pivot] <= target <= nums[-1]:
            return self.binary_search(nums, target, pivot, len(nums) - 1)
        else:
            return self.binary_search(nums, target, 0, pivot - 1)

    def find_pivot(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left

    def binary_search(self, nums: List[int], target: int, left: int, right: int) -> int:
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
