class Solution:
    def rob(self, nums: List[int]) -> int:

        
        mem = {}

        def rob(i):
            if i >= len(nums):
                return 0 
            
            if i in mem:
                return mem[i]
            
            mem[i] = max(rob(i+1) , nums[i] + rob(i+2))
            return mem[i]

        
        return rob(0)


        


        






       



        
        
        
            


        