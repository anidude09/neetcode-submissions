from _heapq import heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        #quick select algorithm 



        # k = len(nums) - k

        # def quicksort(l, r):

        #     pivot, p = nums[r], l 

        #     for i in range(l, r): 
        #         if nums[i] <= pivot : 
        #             nums[p] , nums[i] = nums[i], nums[p]
        #             p += 1
    
        #     nums[p], nums[r] = nums[r], nums[p]
            
        #     if p > k : 
        #         return quicksort(l, p - 1)
        #     elif p < k : 
        #         return quicksort (p + 1, r)
        #     else:
        #         return nums[p] 

        # return quicksort(0, len(nums) - 1)
        
        
        heap = []
        
        for i in nums:
            heapq.heappush(heap, i)

            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

            



        



        
        