class MinStack:
    
    def __init__(self):
        self.s = []
        self.m = []
        
    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.m) == 0:
            self.m.append(val)
        elif len(self.m) > 0 and self.m[-1] >= val:
            self.m.append(val)
            
    def pop(self) -> None:
        if len(self.s) > 0:
            p = self.s.pop()
        if len(self.m) > 0 and self.m[-1] == p:
            self.m.pop()
       
    def top(self) -> int:
        return self.s[-1]
        
    def getMin(self) -> int:
        if len(self.m) > 0:
            return self.m[-1]

    
    

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()