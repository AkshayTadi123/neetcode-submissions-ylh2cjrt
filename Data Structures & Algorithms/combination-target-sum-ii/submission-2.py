class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def helper(index, rem, curr):
            if rem == 0:
                res.append(curr.copy())
                return
                
            if index >= len(candidates) or rem<0:
                return
            
            curr.append(candidates[index])
            helper(index+1, rem - candidates[index], curr)
            curr.pop()

            while index+1<len(candidates) and candidates[index] == candidates[index+1]:
                index+=1
            
            helper(index+1, rem, curr)
        
        helper(0, target, [])
            

        return res