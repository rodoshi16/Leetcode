class Solution:
    def longestPalindrome(self, s: str) -> str:
        #babad - 
        # brute force: find all possible substrings, find if its palindrome
        # 0(n^2)*0(n) 

        # odd, even 
        # iloveracecar
        # pos for both even and odd length palindrome 
        # cbba

        #racecar
        # even: l = i, r = i + 1
        # odd: l = i - 1, r = i + 1

        if len(s) == 0:
            return s

        m = s[0]

        for i in range(len(s)):
            #even
            l = i 
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(m) < r - l + 1:
                    m = s[l:r+1]
                l -= 1
                r += 1
            
            #odd

            l = i - 1 
            r = i + 1 

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if len(m) < r - l + 1:
                    m = s[l:r+1]
                l -= 1
                r += 1
        
        return m





