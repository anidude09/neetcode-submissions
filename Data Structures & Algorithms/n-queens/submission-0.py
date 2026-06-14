class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:


        #postive and negative diagonals
        posDiag = set()
        negDiag = set()
        cols = set()

        board = [["."] * n for i in range(n)]
        result = []

        def backtrack(r):

            if r == n: 
                copy = ["".join(row) for row in board]
                result.append(copy)
                
            
            for c in range(n): 
                
                if (c in cols) or (r - c)  in negDiag or (r + c) in posDiag:
                    continue
                
                posDiag.add(r + c)
                negDiag.add(r - c)
                cols.add(c)
                board[r][c] = "Q"

                backtrack(r+1)

                posDiag.remove(r + c)
                negDiag.remove(r - c)
                cols.remove(c)
                board[r][c] = "."
        
        backtrack(0)

        return result



                

            
            














            











        