class Spreadsheet:
    #26 col, n rows
      
    def __init__(self, rows: int):
        self.s = collections.defaultdict(int)
      
    def setCell(self, cell: str, value: int) -> None:
        self.s[cell] = value
        
    def resetCell(self, cell: str) -> None:
        self.s[cell] = 0
    
    
    def getValue(self, formula: str) -> int:
        #=5+7 , =A2+b2

        f = formula[1:]
        op1, op2 = f.split('+')

        def operand(op):
            if op.isdigit():
                return int(op)
            
            
            return self.s[op]
        
        return operand(op1) + operand(op2)




       







        
        
        



        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)