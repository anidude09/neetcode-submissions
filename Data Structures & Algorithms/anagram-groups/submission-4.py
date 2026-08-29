class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        hash_map = defaultdict(list)

        for word in strs:

            word_map = [0] * 26 

            for char in word:
                word_map[ord(char) - ord('a')] += 1
            
            key = tuple(word_map)
            hash_map[key].append(word)
        
        return list(hash_map.values())

            
            

        