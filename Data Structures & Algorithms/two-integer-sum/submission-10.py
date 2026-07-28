class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            x = nums[i]
            for j in range(i + 1, len(nums)):
                if target - x == nums[j] : 
                    return [i, j]
            








        












        