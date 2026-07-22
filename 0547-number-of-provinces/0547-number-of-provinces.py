class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #input: adj matrix
        # output: no of provinces
        n = len(isConnected)
        m = len(isConnected[0])
        visited = set()
        c = 0 


        for i in range(n):
            for j in range(m):
                if isConnected[i][j] == 1 and (i, j) not in visited:
                    visited.add((i, j))
                    visited.add((j, i))
                    c += 1
        
        return c


        