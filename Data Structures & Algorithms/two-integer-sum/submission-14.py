class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        
        numMap = {}

        for idx, num in enumerate(nums):

            dif = target - num
            if dif in numMap:
                return [numMap[dif], idx]
            
            numMap[num] = idx

        return -1
        