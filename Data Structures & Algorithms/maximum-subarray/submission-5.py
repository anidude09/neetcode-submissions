class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        #kadane's algorithm

        cur = res = nums[0]

        for i in range(1, len(nums)):

            cur = max(nums[i], cur + nums[i])
            res = max(cur, res)
        
        return res

        


        

        

        
