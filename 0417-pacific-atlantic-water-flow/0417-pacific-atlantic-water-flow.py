class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        p = set()
        at = set()

        res = []
    


        def dfs(i, j, visited):
            dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]

            for d in dir:
                    a = i + d[0]
                    b = j + d[1]

                    if 0 <= a < n and 0 <= b < m and (a, b) not in visited and heights[a][b] >= heights[i][j]:
                        visited.add((a, b))
                        dfs(a, b, visited)


        for i in range(m):
            p.add((0, i))
            dfs(0, i, p)
        
        for i in range(n):
            p.add((i, 0))
            dfs(i, 0, p)
        
        for i in range(m):
            at.add((n-1, i))
            dfs(n-1, i, at)
        
        for i in range(n):
            at.add((i, m-1))
            dfs(i, m-1, at)
        
        for (i, j) in p:
            if (i, j) in at:
                res.append([i, j])
        
        return res
        

        

