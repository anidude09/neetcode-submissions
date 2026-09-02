class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:




        memo = {}

        def solve(remain):
            if remain == 0: return 0

            if remain in memo:
                return memo[remain]

            res = float('inf')
            for c in coins:
                if remain - c >= 0 :
                    res = min(res, solve(remain - c) + 1)
            
            memo[remain] = res

            return res
        
        ans = solve(amount)

        return ans if ans != float('inf') else -1