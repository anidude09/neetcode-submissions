class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        seen_num = {}

        for i, num in enumerate(nums):

            dif = target - num

            if dif in seen_num : 

                return [seen_num[dif] , i]
            
            seen_num[num] = i

        return []













        