class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_window = 0
        total_c = len(s)
        freq = defaultdict(int)
        max_freq = 0
        left = 0

        for right in range(total_c):
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])

            if right - left + 1 - max_freq > k:
                freq[s[left]] -= 1
                left += 1

            max_window = max(max_window, right - left + 1)

        return max_window
