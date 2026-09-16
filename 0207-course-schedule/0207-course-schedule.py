class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = {}

        for preq in prerequisites:
            if preq[0] not in adj:
                adj[preq[0]] = [preq[1]]
            else:
                adj[preq[0]].append(preq[1])
        

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
                # if nei in path:
                #     return False
                # if nei not in visited:
                #     dfs(nei)

            path.remove(node)
            visited.add(node)

            return True

    
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

       