import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # start at node
        # append neighbors (price, node, stops)
        # if node == dst and stops -1 <= k 

        d = defaultdict(list)
        cheapest = math.inf

        for u, v, w in flights:
            d[u].append([v, w])
        
        seen = {}
        

        minheap = [(0, src, 0)]

        while minheap:
            price, city, stops = heapq.heappop(minheap)

            if stops > k:
                continue

            for node, w in d[city]:
                if (node, stops+1) not in seen or seen[(node, stops+1)] > price + w:
                    heapq.heappush(minheap, (price + w, node, stops+1))
                
                    seen[(node, stops+1)] = price + w
                
                if node == dst and stops <= k:
                    cheapest = min(cheapest, price + w)

                

        if cheapest == math.inf:
            return -1
        else:
            return cheapest




