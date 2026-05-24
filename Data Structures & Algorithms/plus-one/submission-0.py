class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        initial_str = ""
        for num in digits:
            initial_str += str(num)
        
        initial_num = int(initial_str)
        res = initial_num + 1
        return [int(x) for x in str(res)]