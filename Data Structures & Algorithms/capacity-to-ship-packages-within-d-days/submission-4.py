class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:


        def checkF(n):
            ships = 1
            cap = 0 

            for w in weights:
                if cap + w > n:
                    ships += 1
                    cap = w
                else:
                    cap += w

            return ships <= days

        low = max(weights)
        high = sum(weights)

        while low <= high:
            mid = (high + low) // 2

            if checkF(mid):
                high = mid - 1
            
            else :
                low = mid + 1

        return low




        
        
        









        
        




        