class Solution:
    def jump(self, nums: List[int]) -> int:

        
        memo = {}

        def solve(index):

            if index == len(nums) - 1:
                return 0 
            
            if index in memo:
                return memo[index]
            

            if nums[index] == 0:
                return float('inf')

            res = float('inf')
            end = min(len(nums), index + nums[index] + 1)

            for jump in range(index + 1, end):
                res = min(res, 1 + solve(jump))
            
            memo[index] = res
            return res
        
        return solve(0)
            
