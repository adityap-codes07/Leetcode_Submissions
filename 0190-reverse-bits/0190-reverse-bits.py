class Solution:
    def reverseBits(self, n: int) -> int:
        x = str(bin(n)[2:]).zfill(32)
        revX = ""
        for i in range(len(x)-1, -1, -1):
            revX += (x[i])

        return int(revX, 2)
        