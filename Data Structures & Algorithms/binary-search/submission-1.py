class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = -1
        start = 0
        end = len(nums) - 1
        while (start<=end):
            index = (start+end)//2
            if(nums[index]>target):
                end = index-1
            elif(nums[index]<target):
                start = index+1
            else:
                return index





        return -1