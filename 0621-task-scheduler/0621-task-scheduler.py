import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #find freq and make a max heap
        # pop from heap and store waiting in queue
        # if q is ready - put that back in the heap 

        d = {}
        h = []
        q = deque([])
        t = 0
        for task in tasks:
            if task not in d:
                d[task] = 1 
            else:
                d[task] += 1
        
        for key in d:
            heapq.heappush(h, (-d[key], key))
       
        while h or q:

            if q and q[0][1] <= t:
                pop = q.popleft()
                heapq.heappush(h, (pop[0], pop[2]))

            if h:
                freq, key = heapq.heappop(h)
                if freq + 1 < 0:
                    q.append((freq+1, t + n + 1, key))
                
            
            t += 1

        return t