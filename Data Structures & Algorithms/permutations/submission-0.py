class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        result = []
        path = []
        flag = [False] * len(nums)


        
        def per():
            if len(path) == len(nums):
                result.append(path.copy())
                return
            
            for i , x in enumerate(nums):
                if flag[i]:
                    continue
                
                flag[i] = True
                path.append(x)
                per()
                path.pop()
                flag[i] = False
        
        per()
        return result
                
            

            


        