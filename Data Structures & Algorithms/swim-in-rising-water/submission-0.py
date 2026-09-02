class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:





        rows , cols = len(grid), len(grid[0])

        visited = set()

        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]

        heap = [(grid[0][0], 0, 0)]

        visited.add((0,0))

        while heap:

            t , r, c = heapq.heappop(heap)

            if r == rows - 1 and c == cols - 1:
                return t

            for dr, dc in directions:
                neiR, neiC = dr + r, dc + c

                if min(neiR, neiC) < 0 or neiR == rows or neiC == cols or (neiR, neiC) in visited:
                    continue
                visited.add((neiR, neiC))
                heapq.heappush(heap, (max(t, grid[neiR][neiC]), neiR, neiC))
        
        









        



        
        