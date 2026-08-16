class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        heap = []
        count = defaultdict(int)

        result = []

        for num in nums:
            count[num] += 1
        
        for m in count.keys():
            heapq.heappush(heap, (count[m], m))

            if len(heap) > k:
                heapq.heappop(heap)
            
        
        while heap:
            result.append(heapq.heappop(heap)[1])
        
        return result

        





            

        



        






        



        




        