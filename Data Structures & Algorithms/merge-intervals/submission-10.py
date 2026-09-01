class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        intervals.sort()

        stack = []


        for start, end in intervals:

            while stack and start <= stack[-1][1]:
                start , oldEnd = stack.pop()

                end = max(oldEnd, end)
                
            
            stack.append([start, end])


        return stack






        









    