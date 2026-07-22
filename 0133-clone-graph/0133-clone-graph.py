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
        #input: node
        # 1-2
        #deep vs shallow

        #visited set
        #Node(1) -> Node(2) -> Node(3) -> Node(4)
        #d: mapping from old to new

        d = {}
        visited = set()
        dummy = Node(0)

        if node is None:
            return None

        def dfs(node): 
            visited.add(node)
            if node not in d:
                d[node] = Node(node.val)
            
            for nei in node.neighbors:
                if nei not in visited:
                    dfs(nei)
                d[node].neighbors.append(d[nei])

            dummy.next = d[node]
        
        dfs(node)
        return dummy.next
