class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        best = 0 

        stack = []

        for i, h in enumerate(heights + [0]):

            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0

                width = i - left 
                best = max(best, width * height)
            
            stack.append(i)
        
        return best






        

        