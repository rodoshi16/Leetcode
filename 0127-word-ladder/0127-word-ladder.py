class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set(beginWord)
        c = 1
        word = set(wordList)

        q = deque([beginWord])

        while q:
            l = len(q)
            for _ in range(l):
                t = q.popleft()

                for i in range(len(t)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        new = t[:i] + ch + t[i+1:]

                        if new in word and new not in visited:
                            if new == endWord:
                                return c + 1
                            
                            visited.add(new)
                            q.append(new)
            
            c += 1
    
        return 0 
        