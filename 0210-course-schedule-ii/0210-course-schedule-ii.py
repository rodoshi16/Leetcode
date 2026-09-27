class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
         #return valid course ordering
         # 0 -> 1 -> 2 -> 3
        
        #dict -> stores pre of each class
        #for loop to check visited
        # dfs func

        d = {}
        visited = set()
        path = set()
        ans = []
        for p in prerequisites:
            if p[0] not in d:
                d[p[0]] = [p[1]]
            else:
                 d[p[0]].append(p[1])
        
        def dfs(c):
            if c in visited:
                return True
            
            if c in path:
                return False
        
            path.add(c)
            if c in d:
                for ele in d[c]:
                    if not dfs(ele):
                        return False
                
            visited.add(c)
            path.remove(c)
            ans.append(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
            
        return ans
    
