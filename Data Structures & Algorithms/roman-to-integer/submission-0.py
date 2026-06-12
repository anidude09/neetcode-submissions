class Solution:
    def romanToInt(self, s: str) -> int:

        char = { 
            'I' : 1 ,
            'V' : 5, 
            'X' : 10, 
            'L' : 50,
            'C' : 100, 
            'D' : 500, 
            'M' : 1000
        }

        res = 0 

        for i in range(len(s)): 
            if i + 1 < len(s) and char[s[i]] < char[s[i+1]]:
                res -= char[s[i]]
            else : 
                res += char[s[i]]
        return res

            
            

        