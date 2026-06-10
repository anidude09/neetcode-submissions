class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        #kadane's algorithm

        

        curr = best = nums[0]

        for k in nums[1:]:

            curr = max(k, curr + k)
            best = max(best, curr)

        return best
