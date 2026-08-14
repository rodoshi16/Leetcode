class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #input: nested list of strings
        # output: int 

        n = len(grid)
        m = len(grid[0])
        visited = set()
        dir = [0, 1], [1, 0], [-1, 0], [0, -1]
        count = 0


        def dfs(i, j):
            visited.add((i, j))

            for d in dir:
                a = d[0] + i 
                b = d[1] + j 

                if 0 <= a < n and 0 <= b < m and (a, b) not in visited and grid[a][b] == '1':
                    dfs(a, b)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1' and (i, j) not in visited:
                    dfs(i, j)
                    count += 1 
        
        return count