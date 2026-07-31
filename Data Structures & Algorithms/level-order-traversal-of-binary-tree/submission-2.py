# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ### BFS

        if not root:
            return []
        q = collections.deque()

        q.append(root)

        result = []


        while q:
            q_length =len(q)

            arr = []

            for i in range(q_length):
                node = q.popleft()
                arr.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
            
            result.append(arr)
        

        return result


        

        