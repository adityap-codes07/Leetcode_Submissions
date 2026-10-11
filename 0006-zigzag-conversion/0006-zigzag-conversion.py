class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows > len(s):
            return s

        zigzag = [""] * numRows

        row = 0
        direction = 1

        for ch in s:
            zigzag[row] += ch
            if row == 0:
                direction = 1
            if row == numRows - 1:
                direction = -1
            row += direction
        
        return "".join(zigzag)
