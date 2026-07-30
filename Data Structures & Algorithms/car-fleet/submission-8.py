class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        data = {}
        for p, s in zip(position, speed):
            data[p] = s
        
        sort_pos = sorted(data.keys(), reverse=True)

        time = []
        for k in sort_pos:
            t = (target - k ) / data[k]
            time.append(t)

        stack = []
        stack.append(time[0])

        for i in range(1, len(time)):
            if time[i] > stack[-1]:
                stack.append(time[i])
            

        return len(stack)
            

        
        


        

        
            



        