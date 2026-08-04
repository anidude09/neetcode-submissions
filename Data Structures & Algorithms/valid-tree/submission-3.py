class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adj = {i :[] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        def dfs(node, parent):

            visited.add(node)

            for n in adj[node]:
                if n == parent:
                    continue
                if n in visited:
                    return True
                
                if dfs(n, node):
                    return True
            
            return False

    
        
        if dfs(0, -1):
            return False
        
        if len(visited) != n:
            return False

        return True
                
        

        
        