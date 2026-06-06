class Solution:
    def search(self, nums: List[int], target: int) -> int:


        i = 0
        for num in nums:
            if num == target:
                return i 
            else:
                i += 1
        
        else: 
            return -1
        