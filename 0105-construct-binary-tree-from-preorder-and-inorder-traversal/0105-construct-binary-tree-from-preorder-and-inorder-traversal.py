# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder: [3,9,20,15,7], inorder: [9,3,15,20,7]

        if preorder == [] or inorder == []:
            return None
        
        root = TreeNode(preorder[0])
        t = inorder.index(preorder[0])
        s = len(inorder[:t])
        root.left = self.buildTree(preorder[1:s+1], inorder[:t])
        root.right = self.buildTree(preorder[s+1:], inorder[t+1:])

        return root

        