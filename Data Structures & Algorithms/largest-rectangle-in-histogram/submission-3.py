class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        #monotonically increasing stack
        
        







        

        best = 0 
        stack = []

        for index, height in enumerate(heights + [0]):

            while stack and heights[stack[-1]] > height:

                h = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0 

                width = index - left

                best = max(best, width * h)

            stack.append(index)

        
        return best
