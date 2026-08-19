class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        graph = {i : [] for i in range(numCourses)}
        indeg = [0] * numCourses

        for course, preq in prerequisites:
            graph[preq].append(course)
            indeg[course] += 1
        

        q = collections.deque()

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
            
        result = []
        while q:

            node = q.popleft()

            result.append(node)

            for nei in graph[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        
        if len(result) == numCourses:
            return result
        return []

        