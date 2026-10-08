class Spreadsheet:
    #26 col, n rows
      
    def __init__(self, rows: int):
        self.d = {
            'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
            'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
            'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,
            'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
            'Y': 24, 'Z': 25
        }

        self.s = []
        for i in range(rows):
            self.s.append([0]*26)


    def setCell(self, cell: str, value: int) -> None:
        #A1, B12
        col = cell[0]
        row = int(cell[1:]) - 1


        if row <= len(self.s):
            self.s[row][self.d[col]] = value

    def resetCell(self, cell: str) -> None:
        col = cell[0]
        row = int(cell[1:]) - 1


        if row <= len(self.s):
            self.s[row][self.d[col]] = 0

    
    def getValue(self, formula: str) -> int:
        #=5+7 , =A2+b2

        f = formula[1:]
        op1, op2 = f.split('+')

        def operand(op):
            if op.isdigit():
                return int(op)
            
            col = op[0]
            row = int(op[1:]) - 1
        
            if row <= len(self.s):
                return self.s[row][self.d[col]]
        
        return operand(op1) + operand(op2)




       







        
        
        



        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)