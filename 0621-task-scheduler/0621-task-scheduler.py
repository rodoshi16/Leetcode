import heapq
from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #find freq and make a max heap
        # pop from heap and store waiting in queue
        # if q is ready - put that back in the heap 

        
        h = []
        q = deque([])
        t = 0
        count = Counter(tasks)
        

        
        for task in count:
            h.append((-count[task], task))
        
        heapq.heapify(h)
            
       
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