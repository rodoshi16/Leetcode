class Solution:
    def longestPalindrome(self, s: str) -> str:
        #brute force: 0(n^3)
        # 2 cases, break into half and recurse, miss cbba
        # cbiba
        #for every char, start at middle expand outward if no match, stop otherwise keep expanding outward and store the palindrome 
        if len(s) == 0:
            return s
        
        m = s[0]

        for i in range(len(s)):
            l = i 
            r = i+1
    
            while r < len(s) and l >= 0 and s[l] == s[r]:
                if len(m) < r - l + 1:
                    m = s[l:r+1]
                l -= 1
                r += 1
            
            l = i - 1
            r = i + 1

            while r < len(s) and l >= 0 and s[l] == s[r]:
                if len(m) < r - l + 1:
                    m = s[l:r+1]
                l -= 1
                r += 1
            

        return m


    

    