class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0 
        right = len(nums) - 1

        while left < right: 
            mid = (right + left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            
            else :
                right = mid 


        pivot = left

        def binarysearch(l, r, t):

            while l <= r:
                m = (l+r)//2
                if nums[m] == t:
                    return m 
                elif nums[m] > t:
                    r = m - 1
                else:
                    l = m + 1
            
            return -1
        
        val = binarysearch(pivot, len(nums) - 1, target)
        
        if val != -1:
            return val
        
        return binarysearch(0, pivot - 1, target)
        

            
        
        







        