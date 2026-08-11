class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        seen = set()

        q = collections.deque()
        comp = 0
        for node in range(n):
            
            if node in seen:
                continue
            
            comp += 1
            seen.add(node)
            q.append(node)

            while q:

                node = q.popleft()
                for nei in adj[node]:
                    if nei not in seen:
                        q.append(nei)
                        seen.add(nei)
        
        return comp
            

            







        