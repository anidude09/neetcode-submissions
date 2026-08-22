class Solution:
    def reorganizeString(self, s: str) -> str:


        char_map = collections.defaultdict(int)
        for char in s:
            char_map[char] += 1

        heap = []

        for char in char_map:
            heapq.heappush(heap, (-char_map[char], char))

        
        result = []

        prev_char = ""
        prev_freq = 0
        
    
        while heap:

            freq, char = heapq.heappop(heap)

            freq += 1
            result.append(char)

            
            if prev_freq < 0 :
                heapq.heappush(heap, (prev_freq, prev_char))
            
            prev_freq = freq
            prev_char = char
        
        if len(result) == len(s):
            return "".join(result)
        
        return ""




        

        