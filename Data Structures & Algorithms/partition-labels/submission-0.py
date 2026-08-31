class Solution:
    def partitionLabels(self, s: str) -> List[int]:


        lastIndex = {}

        for index, char in enumerate(s):
            lastIndex[char] = index
        
        size = end = 0 
        result = []

        for index, char in enumerate(s):
            size += 1
            end = max(end, lastIndex[char])

            if index == end:
                result.append(size)
                size = 0 
        
        return result
        