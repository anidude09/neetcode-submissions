class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        adj = {i : [] for i in range(numCourses)}

        for course, preq in prerequisites:
            adj[preq].append(course)

        
        safe = set()
        visiting = set()
        stack = []

        def dfs(node):
            if node in visiting:
                return False
            if node in safe:
                return True

            
            visiting.add(node)

            for n in adj[node]:
                if not dfs(n):
                    return False
                
            visiting.remove(node)
            safe.add(node)
            stack.append(node)

            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return []

        result = []
        while stack:
            print(stack[-1])
            cur = stack.pop()
            print(cur)

            result.append(cur)
            
        return result



        

        


