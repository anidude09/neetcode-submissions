class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def solve(index, total):

            state = (index, total)

            if index == len(nums):
                return 1 if total == target else 0
            if state in memo:
                return memo[state]
            
            add = solve(index + 1, total + nums[index])
            sub = solve(index + 1, total - nums[index])

            memo[state] = add + sub

            return memo[state]

        return solve(0,0)
