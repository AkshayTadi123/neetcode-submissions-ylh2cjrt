class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        look = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                look.remove(nums[l])
                l += 1
            if nums[r] in look:
                return True
            look.add(nums[r])

        return False

