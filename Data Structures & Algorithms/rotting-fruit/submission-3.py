class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        fresh = 0
        q = collections.deque()
        time = 0 

        rows , cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [(-1, 0), (1, 0), (0, 1), (0,-1)]
        if fresh == 0:
            return 0 
        while q:
            if fresh == 0:
                return time
            
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    rd = r + dr
                    cd = c + dc
                    if min(rd, cd) < 0 or rd >= rows or cd >= cols or grid[rd][cd] in (0,2):
                        continue
                    
                    grid[rd][cd] = 2
                    fresh -= 1
                    q.append((rd,cd))
            time += 1
        
        return -1






        