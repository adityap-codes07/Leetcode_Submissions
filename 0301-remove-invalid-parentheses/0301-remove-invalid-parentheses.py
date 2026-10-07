class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        
        balance = 0
        left_remove = 0
        right_remove = 0

        for ch in s:
            if ch == '(':
                balance += 1
            elif ch == ')':
                if balance > 0:
                    balance -= 1
                else:
                    right_remove += 1

        left_remove = balance
        
        ans = []
        path = []

        def validParenthesis(idx, left_remove, right_remove, balance):

            if idx == len(s):
                if left_remove == right_remove == balance == 0:
                    ans.append("".join(path))
                return
            
            ch = s[idx]

            if ch == '(' and left_remove > 0:
                validParenthesis(idx + 1, left_remove - 1, right_remove, balance)

            if ch == ')' and right_remove > 0:
                validParenthesis(idx + 1, left_remove, right_remove - 1, balance)

            if ch != '(' and ch != ')':
                path.append(ch)
                validParenthesis(idx + 1, left_remove, right_remove, balance)

                path.pop()

            elif ch == '(':
                path.append(ch)
                validParenthesis(idx + 1, left_remove, right_remove, balance + 1)

                path.pop()

            else:
                if balance > 0:

                    path.append(ch)
                    validParenthesis(idx + 1, left_remove, right_remove, balance - 1)

                    path.pop()

        validParenthesis(0, left_remove, right_remove, 0)

        return list(set(ans))
