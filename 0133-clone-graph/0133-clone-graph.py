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
        #do dfs
        #create a new graph and connect to rebuild 

        if node is None:
            return None
        
        visited = set()
        d = {}
    
        def dfs(source):
            visited.add(source)
            d[source] = Node(source.val)
            
            
            for nei in source.neighbors:
                if nei not in visited:
                    dfs(nei)
                d[source].neighbors.append(d[nei])
            
        
        dfs(node)
        return d[node]

    
        
        
       

    
        