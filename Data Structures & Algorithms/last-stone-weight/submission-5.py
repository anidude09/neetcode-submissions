class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stone = [-s for s in stones]

        heapq.heapify(stone)
        

        while len(stone) > 1:

            first = heapq.heappop(stone)
            second = heapq.heappop(stone)

            if abs(first - second) > 0:
                heapq.heappush(stone, -abs(first - second))
            
        
        return -stone[0] if stone else 0






        


        