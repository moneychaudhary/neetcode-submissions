class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_array = [c for c in s if c.isalnum()]

        start = 0
        end = len(s_array) - 1

        while start < end:
            if s_array[start] != s_array[end]:
                return False
            start += 1
            end -= 1
        
        return True