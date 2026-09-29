class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        row = len(grid)
        col = len(grid[0])
        if (row + col) % 2 == 0:
            return False
        if grid[0][0] == ")" or grid[row-1][col-1] == "(":
            return False
        seen = {}
        def dfs(r, c, balance):
            if r >= row or c >= col:
                return False
            state =(r, c, balance)
            if grid[r][c] == "(":
                balance += 1
            else:
                balance -= 1

            if balance < 0:
                return False
            if r == row - 1 and c == col - 1:
                return balance == 0
            if balance > (row - 1 - r) + (col - 1 - c):
                return False
            if state in seen:
                return seen[state]

            ans = (
                dfs(r + 1, c, balance) 
                or 
                dfs(r, c + 1, balance)
            )
            seen[state] = ans
            return ans
        return dfs(0, 0, 0)
                