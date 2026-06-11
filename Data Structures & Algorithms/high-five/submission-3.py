class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:

        count = collections.defaultdict(list)

        for data in items: 
            id, score = data 
            count[id].append(score)

        result = [] 

        for id, scores in count.items(): 

            scores.sort(reverse=True)
            result.append([id, (sum(scores[:5]) // 5)])

        
        result.sort(key=lambda x : x[0])
        return result
            
            


        