class MyCircularQueue:
    #last pos connected back to first 
    # FIFO 

    def __init__(self, k: int):
        self.size = k 
        self.q = [None] * k 
        self.front = 0 
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False 
        
        self.rear = (self.rear % self.size)
        self.q[self.rear] = value 
        self.rear += 1
        return True 
        

        
    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.q[self.front] = None
        self.front = (self.front + 1) % self.size
        return True 

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]
        

    def Rear(self) -> int:
        #get the last item of the queue
        if self.isEmpty():
            return -1
        return self.q[(self.rear - 1) % self.size]
        

    def isEmpty(self) -> bool:
        for ele in self.q:
            if ele != None:
                return False
        return True 

    def isFull(self) -> bool:
        if None not in self.q:
            return True 
        return False
       


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()