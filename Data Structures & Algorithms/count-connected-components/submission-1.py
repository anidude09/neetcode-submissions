class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        seen = set()

        stack = []
        comp = 0
        for node in range(n):
            
            if node in seen:
                continue
            
            comp += 1
            seen.add(node)
            stack.append(node)

            while stack:

                node = stack.pop()
                for nei in adj[node]:
                    if nei not in seen:
                        stack.append(nei)
                        seen.add(nei)
        
        return comp
            

            







        