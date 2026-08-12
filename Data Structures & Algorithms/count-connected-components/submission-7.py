class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:


        adj = {i : [] for i in range(n)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        
        q = collections.deque()
        seen = set()
        comp = 0

        for i in range(n):
            if i not in seen:
                q.append(i)
                seen.add(i)
                comp += 1


                while q:
                    node = q.popleft()
                    for nei in adj[node]:
                        if nei not in seen:
                            q.append(nei)
                            seen.add(nei)
        
        return comp







        