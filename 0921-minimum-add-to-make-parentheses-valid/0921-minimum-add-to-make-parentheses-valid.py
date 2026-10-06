class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        bal = 0
        st = []
        for p in s:
            if p == '(':
                st.append(p)
            else:
                if len(st) == 0:
                    bal += 1
                else:
                    st.pop()
        return len(st) + bal
        