class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:


        graph = {i : [] for i in range(numCourses)}
        inorder = [0] * numCourses

        for course, preq in prerequisites:
            graph[preq].append(course)
            inorder[course] += 1
        
        q = collections.deque(i for i in range(numCourses) if inorder[i] == 0)
        out = []


        while q:

            node = q.popleft()
            out.append(q)

            for nei in graph[node]:
                inorder[nei] -= 1
                if inorder[nei] == 0:
                    q.append(nei)
            
        
        if len(out) != numCourses:
            return False
        return True
                
            


        



                