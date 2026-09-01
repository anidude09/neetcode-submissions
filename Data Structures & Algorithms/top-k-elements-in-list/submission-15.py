class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:



        heap = []

        freqMap = defaultdict(int)

        for num in nums:
            freqMap[num] += 1
        
        for num in freqMap:

            heapq.heappush(heap, (freqMap[num], num))

            if len(heap) > k :
                heapq.heappop(heap)
        
        result =[]
        while heap:
            result.append(heapq.heappop(heap)[1])

        return result        