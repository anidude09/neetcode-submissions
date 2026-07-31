class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:



        if not intervals:
            return []

        intervals.sort(key = lambda x : x[0])

        result = [intervals[0]]

        for curr in intervals[1:]:

            last = result[-1]

            if curr[0] <= last[1]:
                curr[0] = last[0]
                curr[1] = max(curr[1], last[1])
                result.pop()

            result.append(curr)
        
        return result
                










    