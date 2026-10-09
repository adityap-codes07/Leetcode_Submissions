class Solution:
    def minInsertions(self, s: str) -> int:
        bal = 0
        ans = 0
        for p in s:
            if p == '(':
                if bal % 2 != 0:
                    bal -= 1
                    ans += 1
                bal += 2
            else:
                bal -= 1
                if bal < 0:
                    ans += 1
                    bal = 1
        return ans + bal
