# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #good: if in the path from root to X no nodes greater than X
        # root counts as 1 and check if its crossed the max seen so far 

        if root is None:
            return 0 
        
        m = root.val 

        def helper(root, m):
            if root is None:
                return 0 
            count = 0 
            if root.val >= m:
                count = 1 
            
            m = max(m, root.val)

            return count + helper(root.left, m) + helper(root.right, m)
        
        return helper(root, m)
