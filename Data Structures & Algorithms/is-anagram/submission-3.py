class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = Counter(s)
        s_count.subtract(t)
        for v in s_count.values():
            if v != 0:
                return False
        return True