class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = 0 

        prefix = {0 : 1}

        curSum = 0 

        for num in nums : 
            curSum += num 

            target = curSum - k 
            if target in prefix : 
                count += prefix[target]
            
            prefix[curSum] = prefix.get(curSum, 0) + 1
            
        return count
            

        