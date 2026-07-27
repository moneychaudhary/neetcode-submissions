class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.visited = set()

        def word_exist(row, col, found):
            if found == word:
                return True

            if (
                row == len(board)
                or col == len(board[0])
                or row < 0
                or col < 0
                or (row, col) in self.visited
            ):
                return False

            self.visited.add((row, col))
            found += board[row][col]
            res = (
                word_exist(row + 1, col, found)
                or word_exist(row - 1, col, found)
                or word_exist(row, col + 1, found)
                or word_exist(row, col - 1, found)
            )
            self.visited.remove((row, col))
            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if word_exist(r, c, ""):
                    return True
        return False
