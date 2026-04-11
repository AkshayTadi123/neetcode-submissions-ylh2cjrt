class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If array is already sorted between left and right
            if nums[left] < nums[right]:
                return nums[left]

            # If middle element is greater than rightmost, minimum is on right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid  # Minimum is at mid or in left half

        return nums[left]
