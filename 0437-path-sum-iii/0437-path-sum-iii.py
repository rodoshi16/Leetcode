# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        #go and visit every path and calcuate the sum along 

        if root is None:
            return 0
        
        def dfs(r, remaining):
            if r is None:
                return 0
            if r.val == remaining:
                count = 1 
            else:
                count = 0 
            
            count += dfs(r.left, remaining - r.val)
            count += dfs(r.right, remaining - r.val)
        
            return count

        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)