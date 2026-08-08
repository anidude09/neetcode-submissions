class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1Copy = nums1[:m]

        i = j = 0
        idx = 0


        while idx < (m+n):

            if j >= n or (i < m and nums1Copy[i] < nums2[j]):
                nums1[idx] = nums1Copy[i]
                i += 1
            else:
                nums1[idx] = nums2[j]
                j += 1
            
            idx += 1
        
        









         
        