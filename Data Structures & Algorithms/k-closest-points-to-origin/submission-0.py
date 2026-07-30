class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:



        heap = []
        i = 0
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (dist, x, y))

        result = []
        while k > 0:
            dist, x, y = heapq.heappop(heap)
            result.append([x,y])
            k -= 1
        
        return result






        
        