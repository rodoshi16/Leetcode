from collections import Counter
import math
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #input: str 
        # f: form as many instances of baloon from text
        # return max number of inputs 
    
        #count frequency of characters
        # nlaebolko: {n: 1, l:2, a: 1, b:1, k:1}
        # b:1 a:1 l:2 o:2 n:1
        # b:2 a:2 l:4 o:4 n:2, n and 2n

        #only count the characters of balloon
        # capped by the minimum number 
        # if any characters of balloon not present, return 0 
    

        d = Counter(text)
        res = math.inf

        for ch in "balloon":
            if ch in "lo":
                n = 2 
            else:
                n = 1 
            
            res = min(res, d[ch]//n)
        
        return res


        