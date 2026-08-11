# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def good(node, preMax):
            if node is None:
                return 0

            g = 1 if node.val >= preMax else 0
            preMax = max(node.val, preMax)

            return g + good(node.left, preMax) + good(node.right,preMax)
        
        return good(root, float('-inf'))
        