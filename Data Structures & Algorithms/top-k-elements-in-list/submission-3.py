class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        count = collections.defaultdict(int)
        buckets = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            count[num] += 1 

        for n, freq in count.items():
            buckets[freq].append(n)
        


        result = []

        
        for i in range(len(buckets) - 1, 0, -1):

            for num in buckets[i]:
                result.append(num)

                if len(result) == k :
                    return result

            

        



        






        



        




        