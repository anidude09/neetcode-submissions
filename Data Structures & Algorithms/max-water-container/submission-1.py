class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_vol = 0

        for i in range(len(heights)):
            for j in range(len(heights)):

                if heights[j] <= heights[i]  and (heights[j] * abs(j-i)) > max_vol : 

                    max_vol = heights[j] * abs(j-i)
                



                

                

        return max_vol
