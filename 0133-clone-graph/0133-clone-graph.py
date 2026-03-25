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
            return node
        
        d = {}
    
        def dfs(source):
            if source in d:
                return d[source]
        
            clone = Node(source.val)
            d[source] = clone
            
            for nei in source.neighbors:
                #take the old node and use that to go through nei 
                #append that to the new guys 
                clone.neighbors.append(dfs(nei))
            
            return clone 
            
    
        return dfs(node)
    
        
        
       

    
        