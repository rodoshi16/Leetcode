from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        #opening -> push to stack 
        # cloing -> pop stack
        # if stack is empty -> true 

        # ( push, ) pop if empty -> FALSE 
        st = []
        d = {"(": ")", "{": "}", "[": "]"}

        for c in s:
            if c in d.keys():
                st.append(c)
            elif c in d.values():
                if not st:
                    return False 
                if d[st.pop()] != c:
                    return False
        
        return not st 



                                                                                                                                                                                                                                           

        