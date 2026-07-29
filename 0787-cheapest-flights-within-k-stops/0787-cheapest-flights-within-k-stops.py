import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        #constraint - k (no of stops)
        # (weight, node)

        # k
        # not checking if no valid path exists
        # do we need cheapest variable

        d = defaultdict(list)
        cheapest = math.inf

        for u, v, w in flights:
            #[1, 100]
            d[u].append([v, w])
        
        minheap = [(0, src, 0)]
        seen = {}

        while minheap:
            price, city, stops = heapq.heappop(minheap)

            if stops > k:
                continue

            for node, w in d[city]:
                if (node, stops+1) not in seen or seen[(node, stops+1)] > price + w:
                    heapq.heappush(minheap, ((price + w), node, stops+1))
                    seen[(node, stops+1)] = price + w
                

                if node == dst:
                    cheapest = min(cheapest, price + w)
        
        if cheapest == math.inf:
            return -1
        else:
            return cheapest
                    


