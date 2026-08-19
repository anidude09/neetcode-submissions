class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:


        result =[]
        path = []


        def dfs(i):
            if len(path) == 4:
                if i == len(s):
                    result.append(".".join(path))
                return
            

            for l in range(1, 4):

                if i + l > len(s):
                    break
                
                segment = s[i:i + l]

                if (len(segment) > 1 and segment[0] == "0") or int(segment) > 255:
                    continue
                
                path.append(segment)
                dfs(i + l)
                path.pop()

        dfs(0)
        return result

        






        
        