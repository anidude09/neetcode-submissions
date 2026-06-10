class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        
        best , count = 0, 0 
        
        for num in nums:
            count = count + 1 if num else 0
            best = max(count, best)
        
        return best
        
        

        
        