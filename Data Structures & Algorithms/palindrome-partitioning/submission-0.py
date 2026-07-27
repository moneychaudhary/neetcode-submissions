class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.results = []

        def is_palindrome(s):
            return s[::-1] == s

        def get_all_parts(index, paritions):
            if index == len(s):
                self.results.append(paritions.copy())
                return

            for j in range(index, len(s)):
                if is_palindrome(s[index : j + 1]):
                    paritions.append(s[index : j + 1])
                    get_all_parts(j + 1, paritions)
                    paritions.pop()

        get_all_parts(0, [])
        return self.results
