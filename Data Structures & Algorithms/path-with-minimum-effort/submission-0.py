class Solution:

    def minimumEffortPath(self, heights: List[List[int]]) -> int:


        cols, rows = len(heights[0]), len(heights)

        grid = [[float('inf')] * cols for _ in range(rows) ]

        grid[0][0] = 0
        drs = [
            (1,0),
            (-1,0),
            (0,1),
            (0,-1)
        ]

        heap = [(0, 0, 0)]

        while heap:
            effort, r, c = heapq.heappop(heap)

            if r == rows - 1 and c == cols - 1:
                return effort
            
            if effort > grid[r][c]:
                continue
            

            for rd, cd in drs:
                dr, dc = r + rd, c + cd
                
                if 0 <= dr < rows and 0 <= dc < cols:

                    diff = abs(heights[dr][dc] - heights[r][c])
                    new_effort = max(effort, diff)

                    if new_effort < grid[dr][dc]:
                        grid[dr][dc] = new_effort

                        heapq.heappush(heap, (new_effort, dr, dc))
            

        