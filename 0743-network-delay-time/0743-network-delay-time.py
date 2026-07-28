from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = defaultdict(list)

        for u, v, w in times:
            d[u].append((v, w))
        
        minheap = [(0, k)]
        visited = set()
        pair = (0, k)
        c = 0

        while minheap:
            t = heapq.heappop(minheap)
            if t[1] in visited:
                continue
            visited.add(t[1])
            c = max(c, t[0])

            for node, w in d[t[1]]:
                if node not in visited:
                    heapq.heappush(minheap, (w + t[0], node))
            
        if len(visited) == n:
            return c
        else:
            return -1