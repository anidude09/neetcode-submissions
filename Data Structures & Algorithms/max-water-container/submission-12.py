class Solution:
    def maxArea(self, heights: List[int]) -> int:


        water = 0 

        left = 0 
        right = len(heights) - 1 

        while left < right:

            if heights[left] < heights[right]:
               h = heights[left]
               w = right - left
               water = max(water, h * w)
               left += 1

            else:
                h = heights[right]
                w = right - left
                water = max(water, h * w)
                right -= 1

        return water 

        