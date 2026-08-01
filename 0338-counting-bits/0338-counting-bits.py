class Solution:
    def countBits(self, n: int) -> List[int]:
        ele = [x for x in range(n+1)]
        res = []
        for i in ele:
            c = 0
            while i > 0:
                if i & 1 == 1:
                    c += 1
                i >>= 1
            res.append(c)
        return res