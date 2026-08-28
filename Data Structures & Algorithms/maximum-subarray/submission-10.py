class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        result = min(nums)
        current = 0 

        for num in nums:
            current = max(num, num + current)
            result = max(result, current)

        return result

        
    


        

        

        
