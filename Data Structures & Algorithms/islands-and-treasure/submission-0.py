class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])

        q = collections.deque()
        visited = set()



        def cellcheck(r, c):
            if min(r,c) < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c] == -1:
                return
            
            visited.add((r,c))
            q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

        
        dist = 0 
        directions = [(-1,0),(1,0), (0,-1), (0,1)]

        while q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                grid[r][c] = dist

                for dr , dc in directions:
                    cellcheck(r + dr, c + dc)
            
            dist += 1
        
        
        






            


        


