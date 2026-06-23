# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
       #both None -> True
       # root is None -> false
       # check root 
       # check left, check right 

        def sameTree(p, q):
            if p is None and q is None:
                return True 
        
            if (p is None and q is not None) or (q is None and p is not None):
                return False
            
            if p.val != q.val:
                return False

            return sameTree(p.left, q.left) and sameTree(p.right, q.right)


        if root is None and subRoot is None:
            return True 
        
        if root is None and subRoot is not None:
            return False 
        
        if sameTree(root, subRoot):
            return True 
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

        


