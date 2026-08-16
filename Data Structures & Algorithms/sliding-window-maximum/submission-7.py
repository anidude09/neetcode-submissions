class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        q = collections.deque()


        result = []

        l = 0 

        for r, val in enumerate(nums):

            while q and nums[q[-1]] <= val:
                q.pop()
            
            l = r - k + 1
            q.append(r)

            if l >= 0 and q[0] < l:
                q.popleft()
            
            if r >= k - 1:
                result.append(nums[q[0]])

        return result