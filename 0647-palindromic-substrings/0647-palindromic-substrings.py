class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 0:
            return 0 
        
        elif len(s) == 1:
            return 1
        
        count = 0
        
        for i in range(len(s)):
            l = i 
            r = i + 1

            while r < len(s) and l >= 0 and s[l] == s[r]:
                count += 1
                l -= 1 
                r += 1
            

            l = i - 1
            r = i + 1

            while r < len(s) and l >= 0 and s[l] == s[r]:
                count += 1
                l -= 1 
                r += 1
           
        return count + len(s)

            

        