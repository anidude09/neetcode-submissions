class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        max_profit = 0

        min = float('inf')

        for price in prices: 
            if price < min : 
                min = price
            
            if price - min > max_profit:
                max_profit = price - min 
    
        return max_profit








             
        