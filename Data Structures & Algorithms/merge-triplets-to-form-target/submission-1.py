class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
       
        shortlist = []
        for x in triplets:
            if x[0]>target[0] or x[1]>target[1] or x[2]>target[2]:
                continue
            shortlist.append(x)

        one = False
        two = False
        three = False

        for x in shortlist:
            if x[0]==target[0]:
                one = True
            
            if x[1]==target[1]:
                two = True
            
            if x[2]==target[2]:
                three = True
        
        return one and two and three
        

