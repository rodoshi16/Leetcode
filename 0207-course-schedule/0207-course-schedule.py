class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        #build adj list
        # run dfs
        # detect cycle on the path 

        adj = {}
        for pre in prerequisites:
            if pre[0] not in adj:
                adj[pre[0]] = [pre[1]]
            else:
                adj[pre[0]].append(pre[1])
        
        visited = set()
        path = set()

        def dfs(node):
            if node in path:
                return False
        
            if node in visited:
                return True 
            
            path.add(node)

            for nei in adj.get(node, []):
                if not dfs(nei):
                    return False
            
            path.remove(node)
            visited.add(node)
            return True 
    
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True

      
        


