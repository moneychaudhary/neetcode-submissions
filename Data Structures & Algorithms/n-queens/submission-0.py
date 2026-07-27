class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.results = []

        def is_safe(row, col, board):
            # Checking in column
            for i in range(n):
                if board[i][col] == "Q":
                    return False

            # Checking in row
            for i in range(n):
                if board[row][i] == "Q":
                    return False

            # Checking in down diagnol:
            i = row
            j = col
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1

            # Checking in up diagnol:
            i = row
            j = col
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1

            return True

        def place(row, board):
            if row == n:
                self.results.append(["".join(r) for r in board])
                return

            for col in range(n):
                if is_safe(row, col, board):
                    board[row][col] = "Q"
                    place(row + 1, board)
                    board[row][col] = "."

        place(0, [["."] * n for i in range(n)])
        return self.results
