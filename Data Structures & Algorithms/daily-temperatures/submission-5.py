class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = []

        for i in range( len(temperatures) - 1):
            
            flag = 0 

            for j in range( i + 1, len(temperatures), 1) :

                if temperatures[j] > temperatures[i] :
                    res.append(j-i)
                    flag = 1
                    break
                
            if flag == 0 : 
                res.append(0)
            
        res.append(0)
        
        return res



        