class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        # memo = {}

        # def solve(index, balance):
        #     if balance == 0:
        #         return 1
        #     if index == len(coins) or balance < 0:
        #         return 0 
            
        #     if (index, balance) in memo:
        #         return memo[(index, balance)]
            
        #     use_coin = solve(index, balance - coins[index])
        #     skip_coin = solve(index + 1, balance)

        #     memo[(index, balance)] = use_coin + skip_coin

        #     return memo[(index, balance)]

        # return solve(0, amount)

        memo = defaultdict(int)
        memo[0] = 1

        for coin in coins:

            for i in range(coin, amount + 1):

                diff = i - coin

                memo[i] += memo[diff] 
            
        return memo[amount]



        






        

        
        