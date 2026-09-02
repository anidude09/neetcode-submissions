class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:



        rows, cols = len(grid), len(grid[0])

        fresh = 0 
        q = collections.deque()

        for r in range(rows):
            for c in range(cols):
                
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        

        if fresh == 0:
            return 0 
        
        time = 0 
        dir = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]

        while q and fresh > 0:

            for _ in range(len(q)):

                r, c = q.popleft()

                for dr, dc in dir:
                    rd, cd = r + dr, c + dc

                    
                    if min(rd, cd) < 0  or rd >= rows or cd >= cols or grid[rd][cd] != 1:
                        continue
                    
                    grid[rd][cd] = 2
                    fresh -= 1

                    q.append((rd, cd))
            
            time += 1
        
        return time if not fresh else -1







        