class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        cols = set()
        posD = set()
        negD = set()
        result = []

        board = [["." for _ in range(n)]  for _ in range(n)]


        def backtrack(r):
            if r == n:
                copy = ["".join(n) for n in board]
                result.append(copy)
            

            for c in range(n):

                if c in cols or (r+c) in posD or (r-c) in negD:
                    continue
                
                board[r][c] = "Q"
                cols.add(c)
                posD.add(r+c)
                negD.add(r-c)
                backtrack(r + 1)
                board[r][c]= "."
                cols.remove(c)
                posD.remove(r+c)
                negD.remove(r-c)
        
        backtrack(0)
        return result
                

            
            



        
        