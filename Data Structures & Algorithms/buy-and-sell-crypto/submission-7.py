class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        profit = 0 
        l = 0

        for r, val in enumerate(prices):
            if val < prices[l]:
                l = r
            
            else :
                profit = max(profit, val - prices[l])


        
        return profit




        