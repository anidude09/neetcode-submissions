class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        # result = []


        # l = r = 0

        # q = collections.deque()


        # while r < len(nums) : 

        #     while q and nums[q[-1]] < nums[r]: 
        #         q.pop()

        #     q.append(r)

        #     if l > q[0] : 
        #         q.popleft()

            
        #     if (r + 1) >= k : 
        #         result.append(nums[q[0]])
        #         l += 1
            
        #     r += 1
        
        # return result 


        result = []

        l = 0 
        r = l + k 
        while r <= len(nums):
            curr = nums[l : r]
            val = max(curr)
            result.append(val)
            l += 1
            r += 1
        
        return result


        











         