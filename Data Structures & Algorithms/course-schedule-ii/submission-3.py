class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        #Kahn's algo

        adj = {i : [] for i in range(numCourses)}

        indeg = [0] * numCourses

        for course, preq in prerequisites:
            adj[preq].append(course)
            indeg[course] += 1


        q = collections.deque()

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        result = []

        while q: 
            node = q.popleft()
            result.append(node)

            for n in adj[node]:
                indeg[n] -= 1

                if indeg[n] == 0:
                    q.append(n)
                
            

        if len(result) == numCourses:
            return result
        
        else:
            return []

            

            
            
            








        

        


