import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        d = defaultdict(list)

        for u, v, w in flights:
            d[u].append((v, w))

        minheap = [(0, src, 0)]  # cost, node, flights used
        stops_seen = {}

        while minheap:
            cost, node, stops = heapq.heappop(minheap)

            if node == dst:
                return cost

            if stops > k:
                continue

            if node in stops_seen and stops_seen[node] <= stops:
                continue

            stops_seen[node] = stops

            for nei, price in d[node]:
                heapq.heappush(
                    minheap,
                    (cost + price, nei, stops + 1)
                )

        return -1





        
        