class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:

        sum_shift = 0 

        for it in shift: 
            dr , amt = it 

            if dr :
                sum_shift -= amt 
            else : 
                sum_shift += amt
        
        sum_shift = sum_shift % len(s)

        
        return s[sum_shift:] + s[:sum_shift]


        
        