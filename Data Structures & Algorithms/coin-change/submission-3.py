class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:


        memo = {}

        def dfs(amount): 

            if amount == 0 :
                return 0 

            coinCount = 1e9

            if amount in memo : 
                return memo[amount] 

            for coin in coins: 
                if amount - coin >= 0 : 
                    coinCount = min(coinCount, 1 + dfs(amount - coin))
            
            memo[amount] = int(coinCount)
            return int(coinCount)

        result = dfs(amount)
        return -1 if result >= 1e9 else result


        


            
            
        

        
            


            

           

        


            


        
        