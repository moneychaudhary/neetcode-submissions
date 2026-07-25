class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        from collections import defaultdict
        first_s_set = defaultdict(int)
        for i in range(len(s)):
            first_s_set[s[i]] = first_s_set[s[i]] + 1
        
        for i in range(len(t)):
            if first_s_set[t[i]] > 0:
                first_s_set[t[i]] =  first_s_set[t[i]] - 1
            else:
                return False
        return True