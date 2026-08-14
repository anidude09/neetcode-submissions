class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        heap = []

        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        for n in count.keys():

            heapq.heappush(heap, (count[n], n))

            if len(heap) > k:
                heapq.heappop(heap)
        

        result = []
        while heap:
            result.append(heapq.heappop(heap)[1])
        
        return result

        





            

        



        






        



        




        