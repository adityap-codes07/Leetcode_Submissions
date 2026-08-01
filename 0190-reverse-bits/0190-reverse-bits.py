class Solution:
    def reverseBits(self, n: int) -> int:
        x = str(bin(n)[2:]).zfill(32)
        return int(x[::-1], 2)
        