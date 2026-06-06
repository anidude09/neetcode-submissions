class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left , right = 0, len(heights) - 1
        
        max_vol = 0  


        while left < right : 

            width = right - left 

            h = min(heights[left], heights[right])

            cap = width * h

            if cap > max_vol:
                max_vol = cap

            if heights[left] < heights[right] :
                left += 1

            else : 
                right -= 1
        
        return max_vol