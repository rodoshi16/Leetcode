class Spreadsheet:
    #26 columns, from A to Z, given number of rows
    #each cell can hold between 0 to 10^5

    def __init__(self, rows: int):
        self.d = {
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
        'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
        'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17,
        'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23,
        'Y': 24, 'Z': 25
        }
        self.spreadsheets = []
        for i in range(rows):
            self.spreadsheets.append([0]*26)

    def setCell(self, cell: str, value: int) -> None:
        #value between 0 and 10^5
        if 0 <= value <= 10**5 and int(cell[1:]) <= len(self.spreadsheets):
            row = int(cell[1:]) -1 
            self.spreadsheets[row][self.d[cell[0]]] = value
        

    def resetCell(self, cell: str) -> None:
        if int(cell[1:]) <= len(self.spreadsheets):
            row = int(cell[1:]) -1
            self.spreadsheets[row][self.d[cell[0]]] = 0
        

    def getValue(self, formula: str) -> int:
        f = formula[1:]

        op1, op2 = f.split("+")

        def operand(op):
            if op.isdigit():
                return int(op)

            row = int(op[1:]) -1
            col = self.d[op[0]]
            return self.spreadsheets[row][col]

        return operand(op1) + operand(op2)





        
        
        



        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)