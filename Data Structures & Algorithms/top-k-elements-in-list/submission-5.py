class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for num in nums: 
            count[num] = count.get(num, 0) + 1

        data = sorted(count.items(), key=lambda x : x[1], reverse=True)
        
        print(data)
        result = []
        for i in range(k):
            result.append(data[i][0])
        

        return result







            

        



        






        



        




        