class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        
        l = 0
        count = defaultdict(int)

        for r , val in enumerate(nums):

            if val in count and (r - l) <=k:
                return True

            count[val] += 1
            
            if r >= k :
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]
                l += 1
        
        return False

            





        