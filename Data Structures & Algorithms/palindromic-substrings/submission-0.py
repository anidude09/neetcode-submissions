class Solution:
    def countSubstrings(self, s: str) -> int:


        def pal(l, r):
            count = 0 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            
            return count
        

        best = 0

        l = r = 0

        while r < len(s):

            best += pal(l,r)
            best += pal(r, r + 1)
            
            l += 1
            r += 1
        
        return best


        


        