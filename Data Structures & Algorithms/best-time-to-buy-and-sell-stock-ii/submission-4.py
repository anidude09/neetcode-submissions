class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # mem = {}

        # def dfs(i, bought): 

        #     if i >= len(prices) : return 0 

        #     if (i, bought) in mem: 
        #         return mem[(i, bought)]

        #     res = dfs(i+1, bought) #skipping, not doing anything (buy or sell)

        #     if bought: 
        #         res = max(res, prices[i] + dfs(i + 1, False))
        #     else:
        #         res = max(res, -prices[i] + dfs(i + 1, True))
        #     mem[(i, bought)] = res
        #     return res
            
        # return dfs(0, False)

        profit = 0 

        for i in range(len(prices)-1): 
            if prices[i + 1] > prices[i]: 
                profit += prices[i+1] - prices[i]
        
        return profit




        
        