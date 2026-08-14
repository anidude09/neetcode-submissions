class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0 
        r = len(heights) - 1
        water = 0 

        while l < r:
            curr = 0 

            if heights[l] < heights[r]:
                curr = (r - l) * heights[l]
                l += 1
            else:
                curr = (r - l) * heights[r]
                r -= 1
            
            water = max(water, curr)
        
        return water


        

        


        