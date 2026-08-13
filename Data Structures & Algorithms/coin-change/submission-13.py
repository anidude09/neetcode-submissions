class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # memo = {}


        # def dfs(amount):

        #     if amount == 0:
        #         return 0 
            
        #     if amount in memo:
        #         return memo[amount]

        #     minCoins = 1e9
            
        #     for c in coins:
        #         if amount - c >= 0 :
        #             minCoins = min(minCoins, 1 + dfs(amount - c))
        #     memo[amount] = minCoins
        #     return minCoins

        # res = dfs(amount)

        # return -1 if res >= 1e9 else res



        memo = [float('inf')] * (amount + 1)
        memo[0] = 0

        for i in range(1, amount + 1):

            
            for c in coins:
                if i - c >= 0:
                    memo[i] = min(memo[i] , memo[i-c] + 1)


        if memo[amount] == float('inf'):
            return -1

        else:
             return memo[amount]            

        


            
            
        

        
            


            

           

        


            


        
        