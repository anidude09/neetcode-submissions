class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []

        nums.sort()


        def solve(index, total, path):

            if total == target:
                result.append(path.copy())


            
            for i in range(index, len(nums), 1):
                if total + nums[i] > target:
                    continue
                
                path.append(nums[i])
                solve(i , total + nums[i], path)
                path.pop()
            
            return
        
        solve(0, 0, [])
        return result