class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:


        dead = set(deadends)

        if target in dead or "0000" in dead:
            return -1

        q = collections.deque()

        q.append(["0000", 0])

        dead.add("0000")


        
         
        
        def build_child(num):

            result = []

            for i in range(4):
                digit = int(num[i])
                posD = (digit + 1) % 10
                negD = (digit - 1) % 10
                for dig in {posD, negD}:
                    pattern = num[:i] + str(dig) + num[i+1:]
                    result.append(pattern)
            return result


    
        while q:

            pattern, turns = q.popleft()

            if pattern == target:
                return turns
            

            for child in build_child(pattern):
                if child not in dead:
                    dead.add(child)
                    q.append([child, turns + 1])

        return -1

                



        




        