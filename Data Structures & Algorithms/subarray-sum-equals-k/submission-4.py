class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        prefix = 0 
        map = {0: 1}
        count = 0 

        for num in nums:
            prefix += num

            target = prefix - k 
            if target in map:
                count += map[target]
            
            map[prefix] = map.get(prefix, 0) + 1
        
        return count
        