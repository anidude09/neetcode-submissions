class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        result = [0] * len(temperatures)
        stack = [] #holds both temp and index


        for i,t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                temp, ind = stack.pop()
                diff = i - ind 
                result[ind] = diff

            
            stack.append([t, i])
        
        return result

        
            





        