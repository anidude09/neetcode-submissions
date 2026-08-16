class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        freqMap = defaultdict(int)

        best = 0 
        l = 0 
        maxFreq = 0 

        for r in range(len(s)):

            freqMap[s[r]] += 1
            maxFreq = max(maxFreq, freqMap[s[r]])

            while (r - l + 1) - maxFreq > k:
                freqMap[s[l]] -= 1
                if freqMap[s[l]] == 0:
                    del freqMap[s[l]]
                l += 1
            
            best = max(best, r - l + 1)
        
        return best




        
        