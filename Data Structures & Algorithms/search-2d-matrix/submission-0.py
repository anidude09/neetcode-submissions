class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        cols = len(matrix[0])
        rows = len(matrix)

        for i in range(rows):
            
            j = 1
            if target <= matrix[i][cols - j]:
                while (cols - j) > -1 : 
                    if target == matrix[i][cols - j]: 
                        return True
                    j += 1
            
        return False 






        



        