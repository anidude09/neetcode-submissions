class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)


        def feasible(rate):
            total = 0 

            for count in piles:
                total += math.ceil(count / rate)
            
            return total <= h
        


        while left <= right:

            mid = (left + right) // 2

            if feasible(mid):
                right = mid - 1
            
            else:
                left = mid + 1
            
        
        return left



        