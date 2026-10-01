class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        sett = set()
        for num in nums:
            temp = []

            for subset in result:
                temp.append(subset + [num])
            
            for x in temp:
                if tuple(sorted(x)) not in sett:
                    sett.add(tuple(sorted(x)))
                    result.append(x)
        return result


