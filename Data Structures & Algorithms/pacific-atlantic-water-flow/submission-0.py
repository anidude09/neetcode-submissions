class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        
        rows, cols = len(heights), len(heights[0])

        atl, pac = set(), set()


        def dfs(r, c, visited, prevHeight):

            if (r,c) in visited or r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prevHeight:
                return
            

            visited.add((r,c))
            prevHeight = heights[r][c]

            for dr, dc in ((-1, 0), (1,0),(0,-1),(0,1)):
                dfs(r + dr, c + dc, visited, prevHeight)
            
        
        for c in range(cols):
            dfs(0, c, pac, -1)
            
            dfs(rows - 1, c, atl, -1)

        for r in range(rows):
            dfs(r, 0, pac, -1)
            dfs(r, cols - 1, atl, -1)

        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r,c) in atl:
                    result.append([r, c])


        return result