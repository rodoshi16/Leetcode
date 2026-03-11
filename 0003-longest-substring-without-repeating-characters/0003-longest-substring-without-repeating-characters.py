class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        "abcabcbb"
        #if duplicate -> include char, shrink window and take length, shift left 
        #otherwise -> increase the window 

        if s == "":
            return 0

        l = 0 
        seen = set()
        m = 0


        for r in range(len(s)):
            while s[r] in seen: 
                seen.remove(s[l])
                l += 1 

            seen.add(s[r])
            m = max(m, len(seen))
        
        return m 
    

"abcabcbb"

            
            





        




