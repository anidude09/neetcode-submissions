class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:


        seen = {0 : -1}

        prefix = 0 


        for idx, val in enumerate(nums):
            prefix += val
            remainder = prefix % k

            if remainder in seen:
                if idx - seen[remainder] >= 2:
                    return True
            else:
                seen[remainder] = idx

        return False
        