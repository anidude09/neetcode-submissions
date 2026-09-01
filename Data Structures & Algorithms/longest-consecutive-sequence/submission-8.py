class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:


        numSet = set(nums)

        length = 0 

        for idx, value in enumerate(nums):

            if idx > 0 and value - 1  in numSet:
                continue
            
            l = 1

            while value + l in numSet:
                l += 1
            
            length = max(length, l)
        
        return length
        