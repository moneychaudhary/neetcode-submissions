class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_window = 0;
        total_c = len(s)
        freq = defaultdict(int)
        max_freq = 0 
        left = 0

        for i in range(total_c):
            freq[s[i]] += 1
            max_freq = max(max_freq, freq[s[i]])


            if i- left + 1 - max_freq > k :
                freq[s[left]] -= 1
                left += 1

            max_window = max(max_window, i- left + 1)

        return max_window





        