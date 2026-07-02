# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def height(root):
            if root is None:
                return 0
            
            return max(height(root.left), height(root.right)) + 1
        
        q = [root]
        m = 0 
        while q:
            d = 0 
            t = q.pop()

            if t.left:
                q.append(t.left)
                d += height(t.left)
    
            if t.right:
                q.append(t.right)
                d += height(t.right)
            
            m = max(m, d)
        return m

        

       
        
        
        
        




        
        
        