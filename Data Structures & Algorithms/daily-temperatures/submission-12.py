class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        stack = []
        result = [0] * len(temperatures)

        for index, value in enumerate(temperatures):

            while stack and stack[-1][1] < value:
                prev_index, _  = stack.pop()

                result[prev_index] = index - prev_index
            
            stack.append((index, value))
        
        return result
        

        