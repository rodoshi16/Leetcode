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


        d = {}
        for ch in text:
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1 
        
        for ch in "balloon":
            if ch not in d :
                return 0

        
        return min(d["b"], d["a"], d["l"]//2, d["o"]//2, d["n"])



       