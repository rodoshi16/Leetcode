import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        
        h = []
        t = []
        for key in d:
            h.append((d[key], key))
        
        heapq.heapify(h)
        
        while len(h) > k :
            heapq.heappop(h)
        
        for tup in h:
            t.append(tup[1])
        
        return t
        




        