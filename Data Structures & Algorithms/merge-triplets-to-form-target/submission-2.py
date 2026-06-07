class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
       
        one, two, three = False, False, False

        for x in triplets:
            if x[0]>target[0] or x[1]>target[1] or x[2]>target[2]:
                continue

            if x[0]==target[0]:
                one = True
            
            if x[1]==target[1]:
                two = True
            
            if x[2]==target[2]:
                three = True

        return one and two and three
        

