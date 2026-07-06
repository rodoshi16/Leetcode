class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        count = 0 
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j):
            visited.add((i, j))
            dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

            for d in dir:
                a = i + d[0]
                b = j + d[1]
                if 0 <= a < n and 0 <= b < m and (a, b) not in visited and grid[a][b] == "1":
                    dfs(a, b)

        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        
        return count

                


        