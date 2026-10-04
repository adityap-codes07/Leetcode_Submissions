class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        idx = 1
        for x in s:
            i = ord(x) - 96
            res += abs(27 - i) * idx
            idx += 1
        return res