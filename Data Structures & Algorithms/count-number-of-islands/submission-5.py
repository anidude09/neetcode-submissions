class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #using DFS search 

        if not grid:
            return 0


        row, col = len(grid), len(grid[0])
        visited = set()
    
        
        def dfs(r, c):
            if (r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == "0" or (r, c) in visited): 
                return 

            visited.add((r, c))
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                dfs(r + dr, c + dc)
            

        count = 0 

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visited:
                    dfs(i, j)
                    count += 1
            
        return count


        






        





        