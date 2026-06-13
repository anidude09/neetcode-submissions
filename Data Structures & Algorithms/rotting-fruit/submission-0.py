class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        
        fresh = 0 
        q = collections.deque()
        time = 0 
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]


        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols): 
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2: 
                    q.append((row, col))

        while fresh > 0 and q: 
            for i in range(len(q)): 
                r, c = q.popleft()
                for dr, dc in directions:
                    rd , cd = r + dr, c + dc
                    if 0 <= rd < rows and 0 <= cd < cols and grid[rd][cd] == 1: 
                        grid[rd][cd] = 2
                        fresh -= 1
                        q.append((rd, cd))


            
            time += 1
        
        return time if fresh == 0 else -1

        
        
        




        



        
        










        