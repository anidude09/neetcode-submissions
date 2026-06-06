# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.dia = 0

        def getD(node):

            if node is None:
                return 0

            left =  getD(node.left)
            right = getD(node.right)
            cur_depth = left + right

            self.dia = max(self.dia , cur_depth)

            return max(left , right) + 1

        getD(root)

        return self.dia
        