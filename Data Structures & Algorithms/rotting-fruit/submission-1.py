class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        fresh = 0
        time = 0

        q = collections.deque()


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]


        while fresh > 0 and q:
            length = len(q)

            for i in range(length):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    if (r + dr) >= 0 and (r + dr) < rows and (c + dc) >= 0 and (c + dc) < cols and grid[r + dr][c + dc] == 1:                 
                        fresh -= 1
                        q.append((r + dr, c + dc))
                        grid[r+dr][c+dc] = 2


            
            time += 1

        if fresh == 0:
            return time

        else :
            return -1

        
         


                

            





        