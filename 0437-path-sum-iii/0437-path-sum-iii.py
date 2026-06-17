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

        def dfs(n, remaining):
            if n is None:
                return 0
            
            if remaining - n.val == 0:
                count = 1 
            else:
                count = 0

            count += dfs(n.left, remaining - n.val)
            count += dfs(n.right, remaining - n.val)
            return count
        
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)

       

    

        

        






















        # count = 0 
        # if root is None:
        #     return 0
        
        # def dfs(node, t):
        #     if node is None:
        #         return 0
        #     count = 0 
        #     if node == t:
        #         count += 1 
            
        #     count += dfs(node.left, t - node.val) 
        #     count += dfs(node.right, t - node.val)

        #     return count 

        # return dfs(root, targetSum)