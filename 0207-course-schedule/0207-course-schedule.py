class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #time: O(v+e) each course and each edge is explored once
        #space: 0(v+e) for the dict and 0(v) + 0(v) for the space
 
        d = defaultdict(list)
        visited = set()
        visiting = set()

        for i in range(numCourses):
            d[i] = []
        for edge in prerequisites:
            d[edge[0]].append(edge[1])
        
        def dfs(node):
            #cycle
            if node in visiting:
                return False
        
            if node in visited:
                return True
            
            visiting.add(node)
            for nei in d[node]:
                if nei not in visited:
                    if not dfs(nei):
                        return False
            
            visited.add(node)
            visiting.remove(node)
            return True


        for key in d:
            if key not in visited:
                if not dfs(key):
                    return False 
        
        return True
            