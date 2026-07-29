class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #using DFS search 

        if not grid:
            return 0


        rows, cols = len(grid), len(grid[0])
        visited = set()
    
        
        def dfs(r, c):
            q = collections.deque()
            q.append((r, c))

            while q : 
                row , col = q.popleft()
                for x , y in [(1,0), (-1, 0), (0,1), (0, -1)]: 
                    rd = row + x
                    cd = col + y
                    if (0 <= rd < rows) and (0<= cd < cols) and grid[rd][cd] == "1" and (rd, cd) not in visited:
                        visited.add((rd, cd))
                        q.append((rd, cd))
            

        count = 0 

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in visited:
                    visited.add((i, j))
                    dfs(i, j)
                    count += 1
            
        return count


        






        





        