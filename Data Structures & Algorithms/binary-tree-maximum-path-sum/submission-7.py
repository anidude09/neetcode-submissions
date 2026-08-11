# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        best = float('-inf')

        def dfs(node):
            nonlocal best

            if node is None:
                return 0
            

            left_total = max(0, dfs(node.left))
            right_total = max(0, dfs(node.right))

            best = max(best, node.val + left_total + right_total)

            return node.val + max(left_total, right_total)
        
        
        dfs(root)
        return int(best)


        

       









        
        