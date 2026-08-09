import heapq
class MedianFinder:
    #odd - middle val
    #even - 2 middle val avg
    #this assumes list is sorted

    def __init__(self):
       self.min = []
       self.max = []

    def addNum(self, num: int) -> None:

        if not self.min or num <= -self.min[0]:
            heapq.heappush(self.min, -num)
        else:
            heapq.heappush(self.max, num)

    
        if len(self.min) > len(self.max) + 1:
                t = -heapq.heappop(self.min)
                heapq.heappush(self.max, t)
        elif len(self.max) > len(self.min) + 1:
                t = heapq.heappop(self.max)
                heapq.heappush(self.min, -t)

        # elif num > -self.min[0] and num < self.max[0]:
        #     if len(self.min) > len(self.max):
        #         heapq.heappush(self.max, num)
        #     else:
        #         heapq.heappush(self.min, -num)



    def findMedian(self) -> float:
        #even, odd
        n = len(self.min) + len(self.max)
        if n % 2 != 0:
            if len(self.min) > len(self.max):
                return -self.min[0]
            else:
                return self.max[0]
        else:
            a = -self.min[0]
            b = self.max[0]
            return (a + b)/2




        
       


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()