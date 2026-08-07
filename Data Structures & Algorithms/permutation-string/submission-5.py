class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        k = len(s1)

        need = [0]* 26
        for char in s1:
            need[ord(char) - ord("a")] += 1

        window = [0] * 26
        for right in range(len(s2)):
            window[ord(s2[right]) - ord("a")] += 1

            if right >= k:
                window[ord(s2[right - k]) - ord("a")] -= 1

            if  window == need:
                return True
        return False
            
            



       




                
                


        
        
         



         
        