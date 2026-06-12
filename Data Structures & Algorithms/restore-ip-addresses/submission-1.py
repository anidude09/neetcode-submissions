class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        result = [] 

        def back(i, dots, curIP): 
            if dots == 4 and i == len(s):
                result.append(curIP[:-1])

            if dots > 4: 
                return 
            
            for j in range(i, min( i+3, len(s))): 

                if int(s[i:j+1]) < 256 and (i == j or s[i] != "0"): 
                    back(j + 1, dots + 1, curIP + s[i:j+1] + ".")
            
        
        
        back(0, 0, "")
        return result


        






        
        