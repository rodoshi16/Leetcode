import heapq
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num: int) -> None:

        if not self.maxHeap or num <= -self.maxHeap[0]:
            heapq.heappush(self.maxHeap, -num)
        else:
            heapq.heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            num = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, num)

        elif len(self.minHeap) > len(self.maxHeap):
            num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -num)
        

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]

        return (-self.maxHeap[0] + self.minHeap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()