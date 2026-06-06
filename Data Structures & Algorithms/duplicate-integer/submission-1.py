class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:


        freq = defaultdict(int)

        for num in nums:
            if freq[num] > 0 : 
                return True
            
            else:
                freq[num] += 1

        return False
        
        