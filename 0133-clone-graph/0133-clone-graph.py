"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        q = [node]
        d = {}

        while q:
            t = q.pop()
            if t not in d:
                d[t] = Node(t.val)
            
            for n in t.neighbors:
                if n not in d:
                    d[n] = Node(n.val)
                    q.append(n)
                
                d[t].neighbors.append(d[n])
        
        return d[node]
        
        