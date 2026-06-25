class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #generate all combinations of well formed parenthesis 
    
        res = []

        def backtrack(current, openn, close):

            if openn == close == n:
                res.append(current)
                return 
            
            if openn < n:
                backtrack(current +"(", openn+1, close)
            
            if close < openn:
                backtrack(current + ")", openn, close+1)
            
        
        backtrack("", 0, 0)
        return res
    


