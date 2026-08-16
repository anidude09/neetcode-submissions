class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:


        q = collections.deque()

        result = []

        for idx, value in enumerate(nums):

            while q and q[0] <= idx - k:
                q.popleft()

            while q and nums[q[-1]] <= value:
                q.pop()
            
            q.append(idx)

            if idx >= k - 1:
                result.append(nums[q[0]])

        return result