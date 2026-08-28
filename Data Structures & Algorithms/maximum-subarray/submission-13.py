class Solution:
    def maxSubArray(self, nums: List[int]) -> int:


        result = nums[0]
        current = 0 

        for num in nums:
            current = max(num, num + current)
            result = max(result, current)

        return result

        
    


        

        

        
