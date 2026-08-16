class Solution:
    def trap(self, height: List[int]) -> int:


        left , right = 0, len(height) - 1

        leftMax = height[left]
        rightMax = height[right]
        water = 0 

        while left < right:

            if leftMax < rightMax:
                left += 1
                leftMax = max(height[left], leftMax)
                water += leftMax - height[left]
                
            else:
                right -= 1
                rightMax = max(height[right], rightMax)
                water += rightMax - height[right]
                
        
        return water

