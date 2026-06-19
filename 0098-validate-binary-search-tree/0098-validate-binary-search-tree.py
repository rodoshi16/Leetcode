# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(root, low, high):
            if root is None:
                return True 

            if not(low < root.val < high):
                return False
            
            return helper(root.left, low, root.val) and helper(root.right, root.val, high)

        
        return helper(root, -inf, inf)
        















        
        # def helper(node, low, high):
        #     if node is None:
        #         return True
        
        #     if not (low <node.val<high):
        #         return False 
            
        #     return helper(node.left, low, node.val) and helper(node.right, node.val, high)
        
        
        # return helper(root, float("-inf"), float("inf"))
        
     
        