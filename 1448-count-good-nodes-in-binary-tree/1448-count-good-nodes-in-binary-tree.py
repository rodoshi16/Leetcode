# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #good: if in the path from root to X no nodes greater than X

        if root is None:
            return 0
        
        m  = root.val
     
        def helper(root, m):
            if root is None:
                return 0
            
            count = 0 
            if root.val >= m:
                count = 1
                
            m = max(root.val, m)

            return count + helper(root.left, m) + helper(root.right, m)
           
        return helper(root, m)




                
