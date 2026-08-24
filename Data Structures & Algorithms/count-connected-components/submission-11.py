class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        graph = {i : [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        

        comp = 0
        visited = set()
        
        def dfs(node):
            if node is None:
                return 
            
            if node in visited:
                return
            
            visited.add(node)
            for nei in graph[node]:
                dfs(nei)
            
            return
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                comp += 1
        
        return comp
        
        