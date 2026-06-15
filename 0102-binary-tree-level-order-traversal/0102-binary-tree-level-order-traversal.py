from collections import deque
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
        
        q = deque([root])
        visited = []


        while q:
            lst = []
            s = len(q)
            t = []

            for i in range(s):
                n = q.popleft()
                lst.append(n.val)
    
                if n.left:
                    t.append(n.left)
                    
                
                if n.right:
                    t.append(n.right)
                    
                
            if lst != []:
                visited.append(lst)
                
            q.extend(t)
    
        return visited



        # if root is None:
        #     return []
        
        # q = [root]
        # visited = [[root.val]]


        # while q:
        #     lst = []
        #     s = len(q)
        #     t = []

        #     for i in range(s):
        #         n = q.pop(0)
    
        #         if n.left:
        #             t.append(n.left)
        #             lst.append(n.left.val)
                
        #         if n.right:
        #             t.append(n.right)
        #             lst.append(n.right.val)
                
        #     if lst != []:
        #         visited.append(lst)
                
        #     q.extend(t)
    
        # return visited

