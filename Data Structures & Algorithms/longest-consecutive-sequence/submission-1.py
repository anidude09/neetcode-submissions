class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num = set(nums)

        streak = 0 


        for n in nums : 

            if (n - 1) not in num : 
                current = n

                curr_streak = 1

                while (current + 1) in num :
                    curr_streak += 1
                    current += 1

                
                streak = max(streak, curr_streak)


        return streak


        