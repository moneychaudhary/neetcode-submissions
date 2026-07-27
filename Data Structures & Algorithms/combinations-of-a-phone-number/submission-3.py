class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        self.results = []
        self.mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def combinations(index, word):
            if index == len(digits):
                self.results.append("".join(word))
                return

            chars = self.mapping[digits[index]]
            for i in range(len(chars)):
                word.append(chars[i])
                combinations(index + 1, word)
                word.pop()

        combinations(0, [])
        return self.results
