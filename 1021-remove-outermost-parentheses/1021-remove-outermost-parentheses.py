class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        st = []
        n = len(s)
        i = 0
        res = []
        for p in range(n):
            if s[p] == "(":
                st.append(s[p])
            else:
                st.pop()
            if len(st) == 0:
                res.append(s[i: p + 1])
                i = p + 1
        ans = ""
        for i in range(len(res)):
            primitive = res[i][1: len(res[i]) - 1]
            ans += primitive
        return ans