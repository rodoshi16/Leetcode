class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        minute = 0 
        visited = set()
        q = []
        c = 0 
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]


        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    c += 1
        
        if c == 0:
            return 0 
        
        while q:
            for _ in range(len(q)):
                t = q.pop(0)
                i = t[0]
                j = t[1]
                visited.add((i, j))


                for d in dir:
                    a = i + d[0]
                    b = j + d[1]

                    if 0 <= a < n and 0 <= b < m and (a, b) not in visited and grid[a][b] == 1:
                        grid[a][b] = 2
                        c -= 1 
                        q.append((a, b))
            
            minute += 1
    
        if c != 0:
            return -1 
        else:
            return minute -1
                    
        