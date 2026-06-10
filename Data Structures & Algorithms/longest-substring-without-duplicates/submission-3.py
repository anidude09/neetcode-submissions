class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        l = 0 
        r = 0 
        char = set()

        best = 0 

        for i in range(len(s)):
            while s[i] in char: 
                char.remove(s[l])
                l += 1
            
            char.add(s[i])

            best = max(best, i - l + 1)
        
        return best
            

        
        

            




        
 

        
            

        