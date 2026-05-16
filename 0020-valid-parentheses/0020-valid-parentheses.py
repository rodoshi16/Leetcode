class Solution:
    def isValid(self, s: str) -> bool:
        d = {"(": ")", "[": "]", "{": "}"}

        st = []
        for i in range(len(s)):
            if s[i] in d:
                st.append(s[i])
            else:
                if len(st) > 0 and st[-1] in d.values():
                    st.append(s[i])
                elif len(st) > 0 and s[i] == d[st[-1]]:
                    st.pop()
                else:
                    return False

        
        return len(st) == 0