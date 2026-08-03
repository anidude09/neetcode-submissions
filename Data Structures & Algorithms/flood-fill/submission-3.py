class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows, cols = len(image), len(image[0])

        org = image[sr][sc]
        visited = set()

        def dfs(r, c):
            
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 
                
            if (r, c) in visited:
                return
            
            if image[r][c] != org:
                return

            visited.add((r,c))
            image[r][c] = color

            for dr, dc in ((-1,0), (1,0), (0,-1), (0,1)):
                dfs(r + dr, c + dc)
            
        
        dfs(sr, sc)

        return image

        


        