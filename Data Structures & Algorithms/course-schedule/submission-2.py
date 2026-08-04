class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        graph = {i : [] for i in range(numCourses)}

        for course, preq in prerequisites:
            graph[course].append(preq)

        

        safe = set()
        visiting = set()

        def dfs(node):
            if node in visiting:
                return False
            
            if node in safe:
                return True
            
            safe.add(node)
            visiting.add(node)

            for n in graph[node]:
                if not dfs(n):
                    return False
            
            visiting.remove(node)

            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        
        return True
        


                