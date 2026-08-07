class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:


        people.sort()

        count , l, r = 0, 0 , len(people) - 1

        while l <= r :
            

            left = limit - people[r]
            count += 1
            r -= 1

            if l <= r and left >= people[l]:
                l += 1
            

        return count