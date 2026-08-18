class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        result = []
        path = []
        flag = [False] * len(nums)


        def per():
            if len(path) == len(nums):
                result.append(path[:])
                return
            

            for idx, val in enumerate(nums):
                if flag[idx]:
                    continue
                flag[idx] = True
                path.append(val)
                per()
                path.pop()
                flag[idx] = False
        

        per()
        return result


        