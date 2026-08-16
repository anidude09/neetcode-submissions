class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        if len(s2) < len(s1):
            return False

        n = len(s1)

        s1map = [0] * 26
        for char in s1:
            s1map[ord(char) - ord('a')] += 1
        
        l = 0 
        s2map = [0] * 26

        
        for r in range(len(s2)):

            s2map[ord(s2[r]) - ord('a')] += 1

            while r - l + 1 > n:
                s2map[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if r >= n - 1:
                if s2map == s1map:
                    return True
        
        return False
        