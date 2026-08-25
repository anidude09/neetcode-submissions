class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:



        total = sum(nums)

        curMax = resMax = nums[0]
        curMin = resMin = nums[0]

        for num in nums[1:]:

            curMax = max(num, curMax + num)
            resMax = max(curMax, resMax)

            curMin = min(num, curMin + num)
            resMin = min(curMin, resMin)

        if resMax < 0:
            return resMax
        
        return max(resMax, total - resMin)
        