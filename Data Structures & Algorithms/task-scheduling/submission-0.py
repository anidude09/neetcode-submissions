class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:





        #formula = max(frame, len(tasks))
        # frame = (maxF - 1) * (cool + 1) + tied


        count = Counter(tasks)

        maxF = max(count.values())
        tied = sum([maxF == freq for freq in count.values()])
        frame = (maxF - 1) * (n + 1) + tied
        return max(len(tasks) , frame)
        


        