class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp={}

        def helper(index, current):
            if(index, current) in dp:
                return dp[(index, current)]

            if(current>amount):
                return 0
            
            if(index == len(coins)):
                return 1 if current == amount else 0
            
            dp[(index, current)] = helper(index, current+coins[index]) + helper(index+1, current)
            return dp[(index, current)]

        return helper(0, 0)
            

            