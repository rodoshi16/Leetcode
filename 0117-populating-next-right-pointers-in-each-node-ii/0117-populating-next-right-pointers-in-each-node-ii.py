from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if root is None:
            return None
        
        q = deque([root])
        visited = []
        while q:
            s = len(q)
            level = []

            for i in range(s):
                n = q.popleft()
                if level != []:
                    level[-1].next = n
                    
                level.append(n)

                if n.left:
                    q.append(n.left)
                
                if n.right:
                    q.append(n.right)
            
            if level != []:
                visited.append(level)

        return root 
        
            


        

        