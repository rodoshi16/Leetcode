import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        
        
        h = []
        t = []
        for key in d:
            if len(h) < k:
                heapq.heappush(h, (d[key], key))
            elif d[key] > h[0][0]:
               heapq.heappop(h)
               heapq.heappush(h, (d[key], key))


        for tup in h:
            t.append(tup[1])
        return t
        




        