class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in d:
                if t[i] in d.values():
                    return False 
                d[s[i]] = t[i]
            else:
                if d[s[i]] != t[i]:
                    return False

        
        return True 

        # if len(s) != len(t):
        #     return False
        # for i in range(len(s)):
        #     #if t maps to something and the key is the not the same as 

        #     if t[i] in d.values() and = 

        #     if s[i] not in d:
        #         d[s[i]] = t[i]
        #     else:
        #         if d[s[i]] != t[i]:
        #             return False
            
        # return True 
            