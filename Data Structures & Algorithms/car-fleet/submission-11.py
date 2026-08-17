class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = []
        for pos, spd in zip(position, speed):
            time = (target - pos) / spd
            pairs.append([pos, time])
        
        pairs.sort(key = lambda x: x[0], reverse=True)
        
        stack = []
        for pos, time in pairs:

            if stack and stack[-1] >= time:
            
                continue
            
            stack.append(time)
        
        return len(stack)



    


        
        
       
        
        


        

        
            



        