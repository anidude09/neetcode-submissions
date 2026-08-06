class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        adj_list = {i : [] for i in range(n)}

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        
        visited = set()

        def dfs(node):

            visited.add(node)

            for n in adj_list[node]:
                if n not in visited:
                    dfs(n)
            

            
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
                
        
        return count

        