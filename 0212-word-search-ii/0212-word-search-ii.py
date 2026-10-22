class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.word = None
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        curr.isWord = True
        curr.word = word


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        n = len(board)
        m = len(board[0])
        out = []
        dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]


        root = TrieNode()
        for w in words:
            root.addWord(w)
        
        def dfs(a, b, node, visited):

            if board[a][b] not in node.children:
                return 
            
            node = node.children[board[a][b]]
            
            if node.isWord:
                out.append(node.word)
                node.isWord = False

            
            visited.add((a, b))
            
            for d in dir:
                r = d[0] + a
                c = d[1] + b 

                if 0 <= r < n and 0 <= c < m and (r, c) not in visited:
                    dfs(r, c, node, visited)
            
            visited.remove((a, b))
            

        for i in range(n):
            for j in range(m):
                dfs(i, j, root, set())
        
        return out 
                    
                    




    
        