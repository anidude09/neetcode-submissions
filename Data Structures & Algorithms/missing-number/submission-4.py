class Solution:
    def missingNumber(self, nums: List[int]) -> int:



        set_num = set(nums)

        l = 0 
        while l < len(nums) + 1: 
            if l not in set_num: 
                return l 

            l += 1

        




            

        
        