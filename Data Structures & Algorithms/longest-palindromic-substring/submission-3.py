class Solution:
    def longestPalindrome(self, s: str) -> str:


        def pal(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            return s[l + 1 : r]
        

        l = 0 
        r = 0

        best = ""
        while r < len(s):

            string1 = pal(l, r)
            string2 = pal(l , r + 1)

            if len(string1) > len(best):
                best = string1
            if len(string2) > len(best):
                best = string2
            
            l += 1
            r += 1

        return best
            





        
        