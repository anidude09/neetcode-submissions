class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}


        def dfs(amount):

            if amount == 0:
                return 0 
            
            if amount in memo:
                return memo[amount]

            minCoins = 1e9
            
            for c in coins:
                if amount - c >= 0 :
                    minCoins = min(minCoins, 1 + dfs(amount - c))
            memo[amount] = minCoins
            return minCoins

        res = dfs(amount)
        return -1 if res >= 1e9 else res




        


            
            
        

        
            


            

           

        


            


        
        