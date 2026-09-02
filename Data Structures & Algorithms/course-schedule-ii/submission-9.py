class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:




        graph = {i : [] for i in range(numCourses)}
        indeg = [0] * numCourses

        for crs, preq in prerequisites:
            graph[preq].append(crs)
            indeg[crs] += 1
        
        q = collections.deque([node for node in range(numCourses) if indeg[node] == 0])

        result = []

        while q : 

            node = q.popleft()
            result.append(node)

            for child in graph[node]:
                indeg[child] -= 1
                if indeg[child] == 0:
                    q.append(child)
            
        return result if len(result) == numCourses else []
        # return result if len(result) == numCourses else []


        