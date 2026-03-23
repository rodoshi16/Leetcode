from collections import defaultdict, deque
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        d = defaultdict(list)
        for i in range(len(graph)):
            d[i].extend(graph[i])
            
        
        paths = []
        path = []
        
        def dfs(node):
            path.append(node)
            
            if node == len(graph) - 1:
                paths.append(path.copy())
        
            for nei in d[node]:
                if nei not in path:
                    dfs(nei)
            path.pop()
            
        dfs(0)
        return paths 
       