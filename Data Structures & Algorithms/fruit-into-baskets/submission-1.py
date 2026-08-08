class Solution:
    def totalFruit(self, fruits: List[int]) -> int:


        left = 0 
        count = defaultdict(int)
        result = 0 

        for right, value in enumerate(fruits):

            count[value] += 1
            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    count.pop(fruits[left])
                left += 1
            
            
            result = max(result, right - left + 1)
            

        return result


            


        
        
