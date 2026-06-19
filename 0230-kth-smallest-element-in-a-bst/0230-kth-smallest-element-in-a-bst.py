# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #root, int k 
        #return kth smallest value of all values of nodes in the tree

        def inorder(root): 
            if root is None:
                return []
            
            return inorder(root.left) + [root.val] + inorder(root.right)
        
        return inorder(root)[k-1]
        
