class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        result = float('-inf')
        current = 0 

        for num in nums:
            current = max(num, num + current)
            result = max(result, current)

        return result

        
    


        

        

        
