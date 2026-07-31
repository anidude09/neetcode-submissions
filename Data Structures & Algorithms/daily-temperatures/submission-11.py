class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp:
                t, id = stack.pop()
                result[id] = i - id

            stack.append([temp, i])

        return result

        
            





        