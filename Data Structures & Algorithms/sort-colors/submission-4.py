class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        #dutch flag algorithm 

        l = mid = 0 
        r= len(nums) - 1


        def swap(i, j): 
            tmp = nums[i] 
            nums[i] = nums[j]
            nums[j] = tmp 

        while mid <= r: 

            if nums[mid] == 0 : 
                swap(l, mid)
                l += 1
            
            elif nums[mid] == 2 : 
                swap(r, mid)
                r -= 1
                mid -= 1

            mid += 1



        

        