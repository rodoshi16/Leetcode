class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #if possible to finish all courses -> return True 
        #if cycle -> return false

        d = defaultdict(list)

        for course, pre in prerequisites:
            d[course].append(pre)

        visited = set()
        visiting = set()

        def dfs(node):

            # Already checked this node before
            if node in visited:
                return True

            # Found a cycle
            if node in visiting:
                return False

            visiting.add(node)

            for nei in d[node]:
                if not dfs(nei):
                    return False

            # Finished exploring this node
            visiting.remove(node)
            visited.add(node)

            return True

        for node in range(numCourses):
            if not dfs(node):
                return False

        return True