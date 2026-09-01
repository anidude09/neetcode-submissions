class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:



        freqMap = defaultdict(int)

        left = 0
        best = 0 

        for right, char in enumerate(s):
            
            freqMap[s[right]] += 1


            while len(freqMap) > k : 
                freqMap[s[left]] -= 1
                if freqMap[s[left]] == 0 :
                    del freqMap[s[left]]
            
                left += 1
            
            best = max(right - left + 1, best)
        
        return best

        