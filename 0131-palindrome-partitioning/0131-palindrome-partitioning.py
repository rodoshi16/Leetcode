class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #aab -> a, a, b, aa, ab, aab
        # "aab" -
        # a -> a -> b
        # aa -> b
        # aab 

        def isp(s):
            left = 0 
            right = len(s) - 1 
            
            while left < right:
                if not s[left].isalnum():
                    left += 1 
                elif not s[right].isalnum():
                    right -=1 
                
                else:
                    if s[right].lower() != s[left].lower():
                        return False 
                
                    left += 1 
                    right -= 1 
            
            return True 

        res = []
        def backtrack(k, current):
            if len(k) == 0:
                res.append(current[:])
                return



            for i in range(len(k)):
                if isp(k[0:i+1]):
                    current.append(k[0:i+1])
                    backtrack(k[i+1:], current)

                    current.pop()

        backtrack(s, [])
        return res


        