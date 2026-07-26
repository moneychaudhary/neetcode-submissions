class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False

    def addWord(self, word):
        current = self
        for w in word:
            if w not in current.children:
                current.children[w] = Trie()
            current = current.children[w]
        current.is_word = True

    def findWord(self, word):
        current = self
        for w in word:
            if w not in current.children:
                return False
            current = current.children[w]
        return current.is_word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS, COLS = len(board), len(board[0])

        trie = Trie()
        for word in words:
            trie.addWord(word)

        answers, visited = set(), set()

        def dfs(r, c, node, word):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visited
                or board[r][c] not in node.children
            ):
                return

            visited.add((r, c))

            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                answers.add(word)

            dfs(r, c - 1, node, word)
            dfs(r, c + 1, node, word)
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)

            visited.remove((r, c))

        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, trie, "")
        return list(answers)
