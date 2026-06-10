class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_map = collections.defaultdict(list)

        for word in strs: 

            sign = "".join(sorted(word))

            hash_map[sign].append(word)

        
        return list(hash_map.values())




            
            

        