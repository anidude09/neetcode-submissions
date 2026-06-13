class Solution:
    def rob(self, nums: List[int]) -> int:

        sums = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0 
            
            if sums[i] != -1: 
                return sums[i]

            sums[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return sums[i]
        

        return dfs(0)

        
        
            


        