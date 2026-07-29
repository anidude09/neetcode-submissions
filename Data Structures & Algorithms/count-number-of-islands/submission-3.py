class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        #using DFS search 
        row, col = len(grid), len(grid[0])
        visited = set()
        count = 0 

        def dfs(i, j):
            dir = [[1,0], [-1,0], [0, 1], [0,-1]]
            q = collections.deque()
            q.append((i, j))
            

            while q: 
                r , c = q.pop()
                for x, y in dir: 
                    rd = r + x
                    cd = c + y 

                    if (0 <= rd < row) and (0<= cd < col) and grid[rd][cd] == "1" and (rd, cd) not in visited: 
                        visited.add((rd, cd))
                        q.append((rd, cd))


        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visited:
                    visited.add((i, j))
                    dfs(i, j)
                    count += 1
            
        return count


        






        





        