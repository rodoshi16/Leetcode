class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        dir = [[1, 0], [0, 1], [0, -1], [-1, 0]]
        count = 0

        def dfs(i, j):
            visited.add((i, j))

            for d in dir:
                a = d[0] + i 
                b = d[1] + j 

                if 0 <= a < n and 0 <= b < m and grid[a][b] == "1" and (a, b) not in visited:
                    dfs(a, b)


        
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        
        return count
       