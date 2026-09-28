class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        ans = 0
        for i in range(len(s)):
            if s[i] == "(":
                cnt += 1
                ans = max(ans, cnt)
            if s[i] == ")":
                cnt -= 1             
        return ans
            