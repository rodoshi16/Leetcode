# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if root is None:
                return 0 
            
            return max(height(root.left), height(root.right)) + 1
    

        if root is None:
            return True
        
        q = [root]

        while q:
            t = q.pop()
            if t.left:
                q.append(t.left)
            if t.right:
                q.append(t.right)
            if abs(height(t.left) - height(t.right)) > 1:
                return False
                
        return True

        