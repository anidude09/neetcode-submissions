class Solution:
    def solve(self, board: List[List[str]]) -> None:


        rows, cols = len(board), len(board[0])

        visited = set()


        def dfs(r, c):
            if (r, c) in visited  or r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != "O":
                return 
            
            visited.add((r,c))
            for dr, dc in ((-1,0),(1,0),(0,-1),(0,1)):
                dfs(r + dr, c + dc)
            

        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)
        
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)
            
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited:
                    board[r][c] = "X"

        







