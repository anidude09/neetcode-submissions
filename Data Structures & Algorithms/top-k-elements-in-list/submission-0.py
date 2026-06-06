class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1

        
        n = len(nums)

        bucket = [[] for _ in range(n + 1)]

        for num, count in freq.items() :
            bucket[count].append(num)
        
        result = []
        for count in range(n,0, -1):
            for num in bucket[count]:
                result.append(num)
                if len(result) == k:
                    return result

        
        return result
        