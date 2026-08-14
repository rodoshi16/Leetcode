class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])
        
        dir = [0, 1], [1, 0], [0, -1], [-1, 0]
        q = []
        minute = 0 
        fresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        while q and fresh > 0:
            size = len(q)

            for i in range(size):
                cell = q.pop(0)

                for d in dir:
                    a = d[0] + cell[0]
                    b = d[1] + cell[1]

                    if 0 <= a < n and 0 <= b < m and grid[a][b] == 1:
                        grid[a][b] = 2
                        fresh -= 1 
                        q.append((a, b))
                
            minute += 1 
            
        if fresh > 0:
            return -1
        return minute






