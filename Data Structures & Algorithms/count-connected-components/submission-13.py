class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        graph = {i : [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        

        comp = 0
        visited = [False] * n
        
        def dfs(node):
            
            if visited[node]:
                return
            
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)
            
            return
        
        for i in range(n):
            if not visited[i]:
                dfs(i)
                comp += 1
        
        return comp
        
        