class Solution:

    def encode(self, strs: List[str]) -> str:
        
        result = []
        for s in strs:
            result.append(str(len(s)))
            result.append("#")
            result.append(s)
        
        return "".join(result)

    def decode(self, s: str) -> List[str]:

        result = []
        n = len(s)
        i = 0

        while i < n :
            start = i 

            while s[i] != "#":
                i += 1
            
            length = int(s[start:i])

            i += 1
            result.append(s[i : i + length])

            i = i + length
        
        return result


