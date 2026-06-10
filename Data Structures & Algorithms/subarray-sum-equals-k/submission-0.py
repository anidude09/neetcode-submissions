class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        result = 0 
        curSum = 0 

        prefixSum = {0 : 1}

        for num in nums: 
            curSum += num

            target = curSum - k 

            if target in prefixSum: 
                result += prefixSum[target]
            
            
            if curSum in prefixSum: 
                prefixSum[curSum] += 1
            else : 
                prefixSum[curSum] = 1
            
        return result



        

            
        