class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:


        memo = {}

        def solve(index, total):
            if index == len(nums):
                return total == target
            
            state = (index, total)

            if state in memo:
                return memo[state]
            

            pos = solve(index + 1, total + nums[index])
            neg = solve(index + 1, total - nums[index])

            memo[state] = pos + neg


            return memo[state]

        
        return solve(0, 0)

        

        