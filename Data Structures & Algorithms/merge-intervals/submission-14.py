class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        intervals.sort(key = lambda x : x[0])

        stack = []

        for start, end in intervals:

            while stack and start <= stack[-1][1]:

                start, oldEnd = stack.pop()

                end = max(oldEnd, end)

            stack.append([start, end])

        
        return stack






        









    