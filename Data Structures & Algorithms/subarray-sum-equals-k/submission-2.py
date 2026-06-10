class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        count = 0 
        sum = 0
        prefix = {0 : 1}

        for num in nums: 
            sum += num
            target = sum - k 
            if target in prefix:
                count += prefix[target]
            
            prefix[sum] = prefix.get(sum, 0) + 1
        
        return count


      

        