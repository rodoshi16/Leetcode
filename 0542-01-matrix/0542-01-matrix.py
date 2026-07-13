class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        visited = set()

        res = []
        for i in range(n):
            res.append([0]*m)
        
        q = []
        

        dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    res[i][j] = 0 
                    q.append((i, j))
                    visited.add((i, j))
    

        while q:
            l = len(q)
            for _ in range(l):
                t = q.pop(0)

                for d in dir:
                    a = t[0] + d[0]
                    b = t[1] + d[1]

                    if 0 <= a < n and 0 <= b < m and (a, b) not in visited:
                        visited.add((a, b))
                        if mat[a][b] != 0:
                            res[a][b] = res[t[0]][t[1]] + 1
                        else:
                            res[a][b] = 0 
                        
                        q.append((a, b))
        
        return res