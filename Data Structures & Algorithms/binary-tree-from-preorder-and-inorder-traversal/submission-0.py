# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inmap = {value : i for i,value in enumerate(inorder)}
        pre = 0 


        def build(left, right):
            nonlocal pre

            if left > right:
                return 
            
            node_val = preorder[pre]
            pre += 1

            root = TreeNode(node_val)

            mid = inmap[node_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root
        
        return build(0, len(preorder) - 1)

         


            

        