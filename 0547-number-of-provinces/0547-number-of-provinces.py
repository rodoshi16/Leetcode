class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #input: adj matrix

        n = len(isConnected)
        m = len(isConnected[0])
        visited = set()
        c = 0 

        def dfs(i, j):
            visited.add((i, j))
            visited.add((j, i))

            for k in range(m):
                if (j, k) not in visited and isConnected[j][k] == 1:
                    dfs(j, k)

        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and (j, i) not in visited and isConnected[i][j] == 1:
                    dfs(i, j) 
                    c += 1

        return c       