class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        # 2 pointer Solution
        
        nums.sort()

        l = 0
        r = len(nums) - 1
        result = -1 

        while l < r :

            total = nums[l] + nums[r]

            if total < k :
                result = max(result, total)
                l += 1

            else:
                r -= 1
            
        
        return result











        



        