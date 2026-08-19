class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        


        graph = {i : [] for i in range(n)}

        for u , v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        count = 0 
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return
            
            visited.add(node)

            for nei in graph[node]:
                if nei == parent:
                    continue
                dfs(nei, node)
            
            return
        
        for i in range(n):
            if i not in visited:
                dfs(i, -1)
                count += 1
        
        return count






        