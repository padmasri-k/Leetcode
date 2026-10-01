class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [["."] * n for i in range(n)]

        def check(row, col):
            for i in range(row):
                if board[i][col] == "Q":
                    return False

                if col - (row - i) >= 0:
                    if board[i][col - (row - i)] == "Q":
                        return False

                if col + (row - i) < n:
                    if board[i][col + (row - i)] == "Q":
                        return False

            return True

        def solve(row):
            if row == n:
                ans.append(["".join(i) for i in board])
                return

            for col in range(n):
                if check(row, col):
                    board[row][col] = "Q"
                    solve(row + 1)
                    board[row][col] = "."

        solve(0)
        return ans