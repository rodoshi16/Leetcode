class MedianFinder:
    #median: middle val in list, even no middle
    #mean of 2 middle vals

    def __init__(self):
        self.l = []
        

    def addNum(self, num: int) -> None:
        self.l.append(num)
        self.l.sort()
        

    def findMedian(self) -> float:
        n = len(self.l)
        i = n // 2
        if n % 2 != 0:
            return self.l[i]
        else:
            return (self.l[i] + self.l[i-1])/2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()