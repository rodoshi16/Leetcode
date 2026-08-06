import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        h = []

        for p in points:
            x2 = p[0]
            y2 = p[1]
            dis = (x2**2 + y2**2) ** 0.5
            h.append((dis, (x2, y2)))
    
        heapq.heapify(h)
        t = []

        while k > 0:
            cor = heapq.heappop(h)[1]
            t.append([cor[0], cor[1]])
            k -=1
        
        return t

        


        