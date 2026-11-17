class Solution:
    def isValid(self, s: str) -> bool:

        d = {'(': ')', '[': ']', '{': '}'}
        st = []

        for ele in s:
            if ele in d:
                st.append(ele)
            elif ele in d.values():

                if st != []:
                    last = st.pop()
                else:
                    return False

                if d[last] != ele:
                    return False
        
        return len(st) == 0
       