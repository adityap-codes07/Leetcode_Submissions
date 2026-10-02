class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        mid = n
        def validParenthesis(n, st, end, paren):
            if len(paren) == n:
                ans.append(paren)
                return
            if st < mid:
                validParenthesis(n, st + 1, end, paren + "(")
            if end < st:
                validParenthesis(n, st, end + 1, paren + ")")

        validParenthesis(2 * n, 0, 0, "")
        return ans