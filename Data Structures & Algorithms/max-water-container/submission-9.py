class Solution:
    def maxArea(self, heights: List[int]) -> int:


        l, r = 0, len(heights) - 1

        area = 0

        while l < r : 

            if heights[l] < heights[r] : 

                ar = heights[l] * ( r - l )

                area = max(area, ar)

                l += 1
            else : 
                ar = heights[r] * (r - l)

                area = max(area, ar)

                r -= 1

        return area



        

        


        