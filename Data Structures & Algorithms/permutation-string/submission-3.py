class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter_s1 = Counter(s1)
        for left in range(len(s2) - len(s1) + 1):
            counter_s2 = Counter(s2[left: left + len(s1)] )
            if counter_s1 == counter_s2:
                return True
        return False
