class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)


        def feasible(rate):
            count = 0
        
            for p in piles:
                count += math.ceil(p/rate)

            return count <= h
        

        while l < r:
            mid = (l + r) // 2

            if feasible(mid):
                r = mid 
            else:
                l = mid + 1
        
        return l

                
        