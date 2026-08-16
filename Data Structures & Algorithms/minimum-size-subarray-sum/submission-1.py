class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        left = 0 
        best = float('inf')
        total = 0

        for r, val in enumerate(nums):

            total += val

            while total >= target:
                best = min(r - left + 1, best)
                total -= nums[left]
                left += 1

        
        
        return int(best) if best < float('inf') else 0






        