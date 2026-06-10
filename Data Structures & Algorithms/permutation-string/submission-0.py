class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        n = len(s1)

        s1_set = collections.defaultdict(int)

        for char in s1:
            s1_set[char] += 1
        
        l = 0 
        r = n - 1

        temp = collections.defaultdict(int)

        while r < len(s2):

            for char in s2[l:r + 1]:
                temp[char] += 1
            
            if temp == s1_set: 
                return True

            l += 1
            r += 1
            temp.clear()
        
        return False



       




                
                


        
        
         



         
        