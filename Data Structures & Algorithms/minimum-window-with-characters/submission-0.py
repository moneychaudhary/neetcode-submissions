class Solution:
    def contains(self, c1: Counter, c2: Counter):
        # If c1 is in c2
        for c in c1:
            if c2[c] < c1[c]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        counter_t = Counter(t)
        window_counter = Counter()

        left = 0
        min_len = float("inf")
        start = 0

        for right in range(len(s)):
            window_counter[s[right]] += 1
            while self.contains(counter_t, window_counter):
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    start = left
                window_counter[s[left]] -= 1
                left += 1

        return s[start : start + min_len] if min_len != float('inf') else ""
