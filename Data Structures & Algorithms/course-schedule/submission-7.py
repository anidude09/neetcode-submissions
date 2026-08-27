class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = {i : [] for i in range(numCourses)}

        for crs, preq in prerequisites:
            graph[preq].append(crs)

        
        visited = set()
        path = set()

        def dfs(node):
            if node in path:
                return False
            
            if node in visited:
                return True
            
            path.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            path.remove(node)

            visited.add(node)
            return True

        for node in range(numCourses):
            if not dfs(node):
                return False
        return True
        