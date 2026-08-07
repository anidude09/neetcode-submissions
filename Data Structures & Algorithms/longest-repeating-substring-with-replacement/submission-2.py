class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        maxF  = 0 
        count = defaultdict(int)
        best = 0 

        left = 0 

        for right, char in enumerate(s):
            count[char] += 1
            maxF = max(maxF, count[char])

            window = right - left + 1
            validRep = window - maxF
            if validRep > k:
                count[s[left]] -= 1
                left += 1
            
            best = max(best, right - left + 1)
        
        return best


