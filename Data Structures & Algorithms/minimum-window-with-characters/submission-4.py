class Solution:
    def minWindow(self, s: str, t: str) -> str:



        if t == "":
            return ""
        
        minL = float('inf')

        tMap = defaultdict(int)
        for char in t:
            tMap[char] += 1
        
        need = len(tMap)
        have = 0 

        result = []


        left = 0 
        
        window = defaultdict(int)

        for right, char in enumerate(s):

            window[char] += 1

            if char in tMap and window[char] == tMap[char]:
                have += 1
            

            while have == need:

                length = right - left + 1

                if length < minL:
                    result = [left , right]
                    minL = length
                
                window[s[left]] -= 1

                if s[left] in tMap and window[s[left]] < tMap[s[left]] :
                    have -= 1
                
                left += 1

            

        

        if result:
            return s[result[0]: result[1]+ 1]
        
        return ""
            
        