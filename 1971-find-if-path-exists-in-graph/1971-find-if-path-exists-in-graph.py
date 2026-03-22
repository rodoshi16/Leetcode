from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
    
        d = defaultdict(list)
        for u,v in edges:
            d[u].append(v)
            d[v].append(u)
        
        visited = set()
        
        def dfs(node):
            visited.add(node)
            if node == destination:
                return True 

            for n in d[node]:
                if n not in visited:
                    if dfs(n):
                        return True
            return False
       
        return dfs(source)
     
            
                
         
            
    
      