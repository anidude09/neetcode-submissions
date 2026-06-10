class Solution:
    def missingNumber(self, nums: List[int]) -> int:



        set_num = set(nums)

        for l in range(0, len(nums) + 1) : 
            if l not in set_num: 
                return l 

        




            

        
        