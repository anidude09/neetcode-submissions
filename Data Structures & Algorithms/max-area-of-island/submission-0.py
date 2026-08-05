class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:


        rows, cols = len(grid), len(grid[0])


        visited = set()

        def dfs(r, c):

            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or (r,c) in visited:
                return 0
            
            visited.add((r,c))  

            directions = [(-1,0), (1,0), (0,-1), (0, 1)]
            ar = 0
            for dr, dc in directions:
                ar +=  dfs(r + dr, c + dc)

            return 1 + ar



        area = 0 
        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    area = max(area, dfs(r,c))

        
        return area
        