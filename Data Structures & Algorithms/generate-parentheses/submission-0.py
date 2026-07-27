class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.results = []

        def get_par(open, closed, subset):
            if open == closed == n:
                self.results.append("".join(subset))
                return

            if open < n:
                subset.append("(")
                get_par(open + 1, closed, subset)
                subset.pop()

            if closed < open:
                subset.append(")")
                get_par(open, closed + 1, subset)
                subset.pop()

        get_par(0, 0, [])
        return self.results
