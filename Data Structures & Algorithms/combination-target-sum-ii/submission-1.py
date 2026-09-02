class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        result = []
        candidates.sort()

        def solve(index, total, path):

            if total == target:
                result.append(path.copy())

            
            for i in range(index, len(candidates)):

                if total + candidates[i] > target:
                    continue
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                solve(i + 1, total + candidates[i], path)
                path.pop()

            
            return
        
        solve(0, 0, [])

        return result
        
            


        