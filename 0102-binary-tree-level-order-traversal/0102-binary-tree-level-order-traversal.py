# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        
        q = [root]
        visited = [[root.val]]


        while q:
            lst = []
            s = len(q)
            t = []

            for i in range(s):
                n = q.pop(0)
    
                if n.left:
                    t.append(n.left)
                    lst.append(n.left.val)
                
                if n.right:
                    t.append(n.right)
                    lst.append(n.right.val)
                
            if lst != []:
                visited.append(lst)
                
            q.extend(t)
    
        return visited


        # if root is None:
        #     return []
        
        # q = [root]
        # lst = [[root.val]]
        # while q:
            
        #     n = q.pop(0)
        #     t = []

        #     if n.left:
        #         q.append(n.left)
        #         t.append(n.left.val)
            
        #     if n.right:
        #         q.append(n.right)
        #         t.append(n.right.val)
            
        #     if t != []:
        #         lst.append(t)
        
        # return lst
    
    