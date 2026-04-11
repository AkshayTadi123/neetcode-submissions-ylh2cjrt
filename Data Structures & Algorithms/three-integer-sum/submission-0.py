class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set();
        numsSort = sorted(nums)
        for i in range(len(numsSort)-2):
            j = i+1
            k = len(numsSort)-1
            target = -numsSort[i]
            while (j<k):
                if(numsSort[j]+numsSort[k]<target):
                    j +=1
                elif(numsSort[j]+numsSort[k]>target):
                    k -= 1
                else:
                    s.add(tuple([numsSort[i], numsSort[j], numsSort[k]]))
                    j += 1

    
        result = [list(t) for t in s]
        return result



