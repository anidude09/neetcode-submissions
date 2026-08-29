class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:


        rows, cols = len(grid), len(grid[0])


        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1
        
        q = collections.deque()
        visited = set()
        
        q.append([0, 0, 1])


        directions = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1),
            (1,1),
            (-1,-1),
            (1,-1),
            (-1,1)
        ]


        while q:

            r, c, path = q.popleft()

            if r == rows - 1 and c == cols - 1:
                return path

            visited.add((r,c))



            for dr, dc in directions:
                
                rd = r + dr
                cd = c + dc

                if min(rd, cd) < 0 or rd >= rows or cd >= cols or (rd, cd) in visited or grid[rd][cd] == 1:
                    continue

                visited.add((rd, cd))
                q.append([rd, cd, path + 1])
        
        return -1
            

            



        