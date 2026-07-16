class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for ele in nums:
            d[ele] = d.get(ele, 0) + 1
        
        res = []
        for key in d:
            heapq.heappush(res, (d[key], key))
            if len(res) > k:
                heapq.heappop(res)
        
        f = []
        for ele in res:
            f.append(ele[1])

        return f
