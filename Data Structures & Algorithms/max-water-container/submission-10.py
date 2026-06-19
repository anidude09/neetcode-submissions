class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0 
        r = len(heights) - 1

        water = 0 

        while l < r :
            cur = 0 
            if heights[l] < heights[r] : 
                cur = heights[l] * ( r - l)
                l += 1

            
            else : 
                cur = heights[r] * (r - l)
                r -= 1
        
            water = max(water, cur)
        
        return water
                



        

        

        


        