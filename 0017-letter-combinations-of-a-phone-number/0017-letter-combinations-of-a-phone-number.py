class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #input: str (digits)
        #output: all possible letter combinations

        dt = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        if digits == "":
            return []

        res = [""]

        for i in range(len(digits)):
            mapp = dt[digits[i]]
            temp = []
            for r in res:
                for j in mapp:
                    temp.append(r + j)
            
            res = temp
                
        return res






            


        



            





                

            





        
