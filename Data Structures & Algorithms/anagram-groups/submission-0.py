class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for str in strs:
            key = tuple(sorted(str))
            anagrams[key].append(str)
            print(key)
        return list(anagrams.values())
