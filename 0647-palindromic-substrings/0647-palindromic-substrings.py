class Solution:
    def countSubstrings(self, s: str) -> int:
        
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

            

        