class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #in: str
        # out: str

        l = 0 
        r = 0 
        tmp = set()
        count = 0


        while r < len(s):
            if s[r] not in tmp:
                tmp.add(s[r])
                count = max(count, r - l + 1)
                r += 1
            else:

                while s[r] in tmp:
                    tmp.remove(s[l])
                    l += 1
        
        return count






        
