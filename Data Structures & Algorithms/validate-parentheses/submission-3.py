class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        stack = []

        for c in s:
            if c in mapping:
                stack.append(mapping[c])
            elif len(stack) > 0 and stack.pop() == c:
                continue
            else:
                return False
        return len(stack) == 0
        