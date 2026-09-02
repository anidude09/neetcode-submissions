class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2

        reachable = [False] * (target + 1)
        reachable[0] = True

        for num in nums:

            for value in range(target, num - 1, -1):
                reachable[value] = reachable[value] or reachable[value - num]
        
        return reachable[target]
        