import operator
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        #input: tokens
        #return an int that represents the value of the expr

        # ["4","13","5","/","+"]
        # 4, 
        # res
        # if you find expr - pop 2 


        # ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
        # [10, 6, ]
        
        s = []

        op = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": lambda a, b: int(a/b)}

        for t in tokens:
            if t not in op:
                s.append(int(t))
            else:
                b = s.pop()
                a = s.pop()

                c = op[t](a, b)
                s.append(c)

        return s[-1]
        